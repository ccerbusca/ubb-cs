package com.ma.lab.entities

import android.graphics.Bitmap
import android.graphics.BitmapFactory
import androidx.room.TypeConverter
import java.io.ByteArrayOutputStream
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter
import java.util.*

class Converters {
    @TypeConverter
    fun fromBitmap(value: Bitmap): ByteArray {
        val stream = ByteArrayOutputStream()
        value.compress(Bitmap.CompressFormat.JPEG, 90, stream)
        return stream.toByteArray()
    }

    @TypeConverter
    fun toBitmap(value: ByteArray): Bitmap =
        BitmapFactory.decodeByteArray(value, 0, value.size)

    @TypeConverter
    fun fromUUID(value: UUID): String = value.toString()

    @TypeConverter
    fun toUUID(value: String): UUID = UUID.fromString(value)

    @TypeConverter
    fun fromLocalDateTime(value: LocalDateTime): String =
        value.format(DateTimeFormatter.ISO_LOCAL_DATE_TIME)

    @TypeConverter
    fun toLocalDateTime(value: String): LocalDateTime =
        LocalDateTime.parse(value, DateTimeFormatter.ISO_LOCAL_DATE_TIME)

    @TypeConverter
    fun fromListOfTags(value: List<String>): String =
        value.joinToString(",")

    @TypeConverter
    fun toListOfTags(value: String): List<String> =
        value.split(',')


}