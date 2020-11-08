package com.ma.lab.repository

import com.ma.lab.entities.ImageEntry
import com.ma.lab.entities.ImageEntryDao

class ImageEntryRepo(private val imageEntryDao: ImageEntryDao) {

    val entries = imageEntryDao.getEntries()

    suspend fun addEntry(entry: ImageEntry) {
        imageEntryDao.insert(entry)
    }

    suspend fun deleteEntry(entry: ImageEntry) {
        imageEntryDao.delete(entry)
    }

    suspend fun updateEntry(entry: ImageEntry) {
        imageEntryDao.update(entry)
    }
}