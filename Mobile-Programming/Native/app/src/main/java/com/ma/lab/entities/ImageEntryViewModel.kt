package com.ma.lab.entities

import android.app.Application
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.LiveData
import androidx.lifecycle.viewModelScope
import com.ma.lab.repository.ImageEntryRepo
import kotlinx.coroutines.launch

class ImageEntryViewModel(application: Application) : AndroidViewModel(application) {

    private val repo: ImageEntryRepo

    val entries: LiveData<List<ImageEntry>>

    init {
        val entriesDao = ImageEntriesRoomDB.getDatabase(application, viewModelScope).entryDao()
        repo = ImageEntryRepo(entriesDao)
        entries = repo.entries
    }

    fun insert(entry: ImageEntry) = viewModelScope.launch {
        repo.addEntry(entry)
    }

    fun delete(entry: ImageEntry) = viewModelScope.launch {
        repo.deleteEntry(entry)
    }

    fun update(entry: ImageEntry) = viewModelScope.launch {
        repo.updateEntry(entry)
    }

}