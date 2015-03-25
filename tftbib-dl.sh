#!/bin/bash

books="Genesis Exodus Leviticus Numbers Deuteronomy Joshua Judges Ruth 1Samuel 2Samuel 1Kings 2Kings 1Chronicles 2Chronicles Ezra Nehemiah Esther Job Psalms Proverbs Ecclesiastes SongOfSolomon Isaiah Jeremiah Lamentations Ezekiel Daniel Hosea Joel Amos Obadiah Micah Nahum Habakkuk Zephaniah Zechariah Malachi Matthew Mark Luke John Acts Romans 1Corinthians 2Corinthians Galatians Ephesians Philippians Colossians 1Thessalonians 2Thessalonians 1Timothy 2Timothy Titus Philemon Hebrews James 1Peter 2Peter 1John 23John Jude Revelation";

urlfile="urlist.txt"
for book in $books; do
    if [[ -d "$book" ]]; then	
	cd $book
	if [[ -f "$urlfile" ]]; then
	    # $CMD "urlist.txt"
	    printf '%s\n' "File $urlfile exists."
	    aria2c -i $urlfile
	fi
	cd ".."
    fi
done
