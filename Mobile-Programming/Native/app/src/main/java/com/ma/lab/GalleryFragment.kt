package com.ma.lab

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import androidx.navigation.fragment.findNavController
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.ma.lab.entities.ImageEntry
import com.ma.lab.entities.ImageEntryViewModel
import kotlinx.android.synthetic.main.fragment_first.*

/**
 * A simple [Fragment] subclass as the default destination in the navigation.
 */
class GalleryFragment : Fragment() {

    private lateinit var imageEntryViewModel: ImageEntryViewModel

    override fun onCreateView(
            inflater: LayoutInflater, container: ViewGroup?,
            savedInstanceState: Bundle?
    ): View? {
        val ll = inflater.inflate(R.layout.fragment_first, container, false)

        ll.findViewById<RecyclerView>(R.id.recycler_view)

        return ll
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        val adapterRecyclerView = AdapterRecyclerView(requireContext(), object : CardListener {
            override fun onDeleteButtonClick(entry: ImageEntry) {
                imageEntryViewModel.delete(entry)
            }

            override fun onEditButtonClick(entry: ImageEntry) {
                val bundle = Bundle()
                bundle.putSerializable("entity", entry)

                val addUpdateFragment = AddUpdateFragment()
                addUpdateFragment.arguments = bundle
                findNavController().navigate(R.id.action_FirstFragment_to_SecondFragment, bundle)
            }
        })
        recycler_view.apply {
            layoutManager = LinearLayoutManager(context)
            adapter = adapterRecyclerView
        }
        imageEntryViewModel = ViewModelProvider(this).get(ImageEntryViewModel::class.java)

        imageEntryViewModel.entries.observe(viewLifecycleOwner, Observer { entries ->
            entries?.let { adapterRecyclerView.setEntries(it) }
        })

    }
}