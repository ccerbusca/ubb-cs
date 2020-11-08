package com.ma.lab

import com.ma.lab.entities.ImageEntry

interface CardListener {

    fun onEditButtonClick(entry: ImageEntry)

    fun onDeleteButtonClick(entry: ImageEntry)

}