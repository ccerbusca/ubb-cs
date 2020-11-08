package com.ma.lab.entities

import android.os.Parcelable
import androidx.room.Entity
import androidx.room.PrimaryKey
import androidx.room.TypeConverters
import kotlinx.android.parcel.Parcelize
import java.io.Serializable
import java.time.LocalDateTime
import java.util.*

@Parcelize
@Entity(tableName = "entry_table")
@TypeConverters(Converters::class)
data class ImageEntry(var title: String,
                      var description: String,
                      var tags: List<String>,
                      var image: ByteArray,
                      var dateAdded: LocalDateTime = LocalDateTime.now(),
                      @PrimaryKey var id: UUID = UUID.randomUUID()) : Serializable, Parcelable {
    override fun equals(other: Any?): Boolean {
        if (this === other) return true
        if (javaClass != other?.javaClass) return false

        other as ImageEntry

        if (title != other.title) return false
        if (description != other.description) return false
        if (tags != other.tags) return false
        if (!image.contentEquals(other.image)) return false
        if (dateAdded != other.dateAdded) return false
        if (id != other.id) return false

        return true
    }

    override fun hashCode(): Int {
        var result = title.hashCode()
        result = 31 * result + description.hashCode()
        result = 31 * result + tags.hashCode()
        result = 31 * result + image.contentHashCode()
        result = 31 * result + dateAdded.hashCode()
        result = 31 * result + id.hashCode()
        return result
    }
}