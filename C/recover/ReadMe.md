# Recover

retrieving deleted images from an empty camera card.

## Background

In the computer world, "deleted" tends not to mean "deleted" so much as "forgotten". In this problem set students are required to take an empty camera card, card.raw, and retrieve all the deleted images from it.

## JPEG

### Signatures

Even though JPEGs are more complicated than BMPs, JPEGs have **"signatures"**, patterns of bytes that can distinguish them from other file formats. Specifically, the first three bytes of JPEGs are

> 0xff 0xd8 0xff

The fourth byte, meanwhile, starts with `0xe` meaning that the first 4 bits of the fourth byte are 1110. To be fair, you might encounter these patterns on some disk purely by chance, so data recovery isn’t an exact science.

### camera storage

digital cameras tend to store photographs contiguously on memory cards, whereby each photo is stored immediately after the previously taken photo. Accordingly, the start of a JPEG usually demark the end of another. digital cameras often initialize cards with a **FAT file system** whose **"block size"** is 512 bytes (B). The implication is that these cameras only write to those cards in units of 512 B.

For example, a photo that’s 1 MB (i.e., 1,048,576 B) thus takes up 1048576 ÷ 512 = 2048 **"blocks"** on a memory card. But so, does a photo that’s, say, one byte smaller (i.e., 1,048,575 B)! The wasted space on disk is called **"slack space"**.

on a side note, Forensic investigators often look at slack space for remnants of suspicious data.

Thanks to FAT, we can trust that JPEGs' signatures will be **"block-aligned"**. That is, we need only look for those signatures in a block’s first four bytes. brand-new memory cards have probably been **"zeroed"** (i.e., filled with 0s) by the manufacturer, in which case any slack space will be filled with 0s.

## Usage

```bash
$ ./recover card.raw
$
```

The program takes in a camera card as a command-line argument and retrieves any of the card's deleted photos.

## Recovered

The camera card had exactly 50 deleted photos are of which are stored in the [`recovered directory`](recovered).
