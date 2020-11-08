package com.ma.lab.entities

import androidx.lifecycle.LiveData
import androidx.room.*

@Dao
interface ImageEntryDao {

    @Query("SELECT * from entry_table")
    fun getEntries(): LiveData<List<ImageEntry>>

    @Insert(onConflict = OnConflictStrategy.IGNORE)
    suspend fun insert(entry: ImageEntry)

    @Update(onConflict = OnConflictStrategy.IGNORE)
    suspend fun update(entry: ImageEntry)

    @Delete(entity = ImageEntry::class)
    suspend fun delete(entry: ImageEntry)

    @Query("DELETE FROM entry_table")
    suspend fun deleteAll()

}