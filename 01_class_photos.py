def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)
    if redShirtHeights[0] > blueShirtHeights[0]:
        back_row = redShirtHeights
        front_row = blueShirtHeights
    else:
        back_row = blueShirtHeights
        front_row = redShirtHeights
    for i in range(len(back_row)):
        if front_row[i] >= back_row[i]:
            return False
    return True
