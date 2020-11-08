package com.ma.lab.entities

import android.content.Context
import androidx.room.Database
import androidx.room.Room
import androidx.room.RoomDatabase
import androidx.sqlite.db.SupportSQLiteDatabase
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch

@Database(entities = [ImageEntry::class], version = 2)
abstract class ImageEntriesRoomDB : RoomDatabase() {

    abstract fun entryDao(): ImageEntryDao

    companion object {
        @Volatile
        private var instance: ImageEntriesRoomDB? = null

        fun getDatabase(context: Context, scope: CoroutineScope): ImageEntriesRoomDB {
            return instance ?: synchronized(this) {
                val instance = Room.databaseBuilder(
                    context.applicationContext,
                    ImageEntriesRoomDB::class.java,
                    "image_entry_database"
                )
                    .fallbackToDestructiveMigration()
                    .addCallback(ImageEntryDBCallback(scope))
                    .build()
                Companion.instance = instance
                instance
            }
        }

        private class ImageEntryDBCallback(
            private val scope: CoroutineScope
        ) : RoomDatabase.Callback() {
            override fun onOpen(db: SupportSQLiteDatabase) {
                super.onOpen(db)
//                instance?.let {
//                    scope.launch(Dispatchers.IO) {
//                        it.entryDao().deleteAll()
//                    }
//                }
            }
        }
    }

}