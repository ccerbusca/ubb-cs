package com.ma.lab

import android.content.Context
import android.graphics.BitmapFactory
import android.graphics.drawable.BitmapDrawable
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import androidx.core.content.ContextCompat
import androidx.navigation.fragment.NavHostFragment
import androidx.recyclerview.widget.RecyclerView
import com.google.android.material.chip.Chip
import com.google.android.material.chip.ChipGroup
import com.ma.lab.entities.ImageEntry
import kotlinx.android.synthetic.main.list_item.*
import kotlinx.android.synthetic.main.list_item.view.*

class AdapterRecyclerView internal constructor(
    private val context: Context, private val cardListener: CardListener
) : RecyclerView.Adapter<AdapterRecyclerView.ViewHolder>() {

    private val inflater = LayoutInflater.from(context)
    private var items = emptyList<ImageEntry>()

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        return ViewHolder(inflater.inflate(R.layout.list_item, parent, false))
    }

    override fun getItemCount() = items.size

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.bindData(items[position], context)

        holder.itemView.edit_button.setOnClickListener {
            cardListener.onEditButtonClick(items[position])
        }

        holder.itemView.delete_button.setOnClickListener {
            cardListener.onDeleteButtonClick(items[position])
        }
    }

    internal fun setEntries(entries: List<ImageEntry>) {
        items = entries
        notifyDataSetChanged()
    }

    inner class ViewHolder(view: View) : RecyclerView.ViewHolder(view) {
        private val cardImgView: ImageView = view.imageView
        private val titleTextView: TextView = view.card_title
        private val subtitleTextView: TextView = view.card_subtitle
        private val chipGroup: ChipGroup = view.chip_group

        fun bindData(imageEntry: ImageEntry, context: Context) {
            cardImgView.setImageBitmap(
                BitmapFactory.decodeByteArray(imageEntry.image, 0, imageEntry.image.size))
            titleTextView.text = imageEntry.title
            subtitleTextView.text = imageEntry.description

            imageEntry.tags.forEach {
                val chip = Chip(context)
                chip.text = it
                chipGroup.addView(chip)
            }
        }
    }
}