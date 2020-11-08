package com.ma.lab

import android.app.Activity
import android.content.Intent
import android.graphics.Bitmap
import android.graphics.BitmapFactory
import android.graphics.ImageDecoder
import android.graphics.drawable.BitmapDrawable
import android.os.Bundle
import android.text.Editable
import android.text.Spanned
import android.text.TextWatcher
import android.text.style.ImageSpan
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.Toast
import androidx.activity.addCallback
import androidx.fragment.app.Fragment
import androidx.lifecycle.ViewModelProvider
import androidx.navigation.fragment.findNavController
import com.google.android.material.button.MaterialButton
import com.google.android.material.chip.ChipDrawable
import com.google.android.material.textfield.TextInputLayout
import com.ma.lab.entities.ImageEntry
import com.ma.lab.entities.ImageEntryViewModel
import com.ma.lab.repository.ImageEntryRepo
import kotlinx.android.synthetic.main.fragment_second.*
import kotlinx.android.synthetic.main.list_item.*
import kotlinx.android.synthetic.main.list_item.view.*
import java.io.ByteArrayOutputStream
import java.io.IOException
import kotlin.properties.Delegates

const val IMAGE_REQUEST_CODE = 777

class AddUpdateFragment : Fragment() {

    private lateinit var imageEntryViewModel: ImageEntryViewModel
    private var imageBitmap: Bitmap? = null
    private var entity: ImageEntry? = null

    override fun onCreateView(
            inflater: LayoutInflater, container: ViewGroup?,
            savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment

        entity = arguments?.getSerializable("entity") as ImageEntry?

        val ll = inflater.inflate(R.layout.fragment_second, container, false)
        setUpTagInput(ll)
        setUpImageUpload(ll)

        return ll
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        imageEntryViewModel = ViewModelProvider(this).get(ImageEntryViewModel::class.java)

        if (entity != null) {
            title_input.editText!!.setText(entity!!.title)
            description_input.editText!!.setText(entity!!.description)
            entity!!.tags.forEach {
                tags_input.editText!!.text.append("$it ")
            }


            val bitmap = BitmapFactory.decodeByteArray(entity!!.image, 0, entity!!.image.size)
            image_upload.setImageBitmap(bitmap)
            imageBitmap = bitmap
        }

        save_button.setOnClickListener {
            if (validateInputs()) {
                val entry = ImageEntry(
                    title = title_input.editText!!.text.toString(),
                    description = description_input.editText!!.text.toString(),
                    tags = tags_input.editText!!.text.toString()
                        .trim().split("\\s".toRegex()).filter { !it.isBlank() },
                    image = bitmapToByteArray(imageBitmap!!)
                )

                if (entity != null) {
                    entry.id = entity!!.id
                    entry.dateAdded = entity!!.dateAdded
                    imageEntryViewModel.update(entry)
                } else {
                    imageEntryViewModel.insert(entry)
                }

                findNavController().popBackStack()
            }
        }
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        if (requestCode == IMAGE_REQUEST_CODE &&
            resultCode == Activity.RESULT_OK &&
            data != null &&
            data.data != null
        ) {
            val imageUri = data.data
            try {
                val source = ImageDecoder.createSource(requireActivity().contentResolver, imageUri!!)
                imageBitmap = ImageDecoder.decodeBitmap(source)
                image_upload.setImageBitmap(imageBitmap)
            } catch (e: IOException) {
                e.printStackTrace()
            }
        }
    }

    private fun validateInputs(): Boolean {
        return if (title_input.editText!!.text.isNotBlank() &&
            description_input.editText!!.text.isNotBlank() &&
            tags_input.editText!!.text.isNotBlank() &&
            imageBitmap != null)
            true
        else {
            Toast.makeText(context, "Missing some data", Toast.LENGTH_SHORT).show()
            false
        }
    }

    private fun bitmapToByteArray(bitmap: Bitmap): ByteArray {
        val stream = ByteArrayOutputStream()
        bitmap.compress(Bitmap.CompressFormat.JPEG, 90, stream)
        return stream.toByteArray()
    }

    private fun setUpImageUpload(ll: View) {
        ll.findViewById<ImageView>(R.id.image_upload).setOnClickListener { openPhoneGallery() }
        ll.findViewById<MaterialButton>(R.id.image_upload_button).setOnClickListener { openPhoneGallery() }
    }

    private fun openPhoneGallery() {
        val intent = Intent()
        intent.type = "image/*"
        intent.action = Intent.ACTION_GET_CONTENT
        this.startActivityForResult(Intent.createChooser(intent, "Please Select Image"), IMAGE_REQUEST_CODE)
    }

    private fun setUpTagInput(ll: View) {
        val text = ll.findViewById<TextInputLayout>(R.id.tags_input).editText!!


        text.addTextChangedListener(object : TextWatcher {
            private var lastIndex = 0;

            override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {}

            override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) {}

            override fun afterTextChanged(s: Editable?) {
                val editable = s!!
                if (editable.endsWith(' ') && editable.length > 2 && editable.length > lastIndex &&
                    editable[editable.length - 2] != ' ') {
                    val subSequence = editable.subSequence(lastIndex, editable.length - 1).trim()

                    val drawable = ChipDrawable.createFromResource(requireContext(), R.xml.standalone_chip)
                    drawable.isCloseIconVisible = false
                    drawable.text = subSequence
                    drawable.setBounds(0, 0, drawable.intrinsicWidth, drawable.intrinsicHeight)
                    val span = ImageSpan(drawable)
                    val editableText = text.text!!
                    editableText.setSpan(span, lastIndex, editableText.length, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE)
                    lastIndex = editable.length
                }
                if (editable.length < lastIndex) {
                    lastIndex = editable.length
                }
            }

        })
    }
}