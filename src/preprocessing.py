"""
Preprocessing Function for Template matching.It consist two function,
one for extract segment from the input image. Second matches the cropped
template with actual template image
"""

import cv2
import dask

import numpy as np


@dask.delayed
def segment_image(image_path):
    """
    Generate the list of segmented cropped image
    from the input image as template

    Parameters
    ----------
    image_path : str
        input image path

    Returns
    -------
    list
        list of segmented cropped images as a template
    """
    image_array = cv2.imread(image_path)
    image_array = cv2.resize(image_array, (2048, 2048))
    gray_image = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(
        gray_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )
    # assign a rectangle kernel size
    kernel = np.ones((5, 5), "uint8")
    margin_img = cv2.dilate(threshold, kernel, iterations=4)

    (contours, _) = cv2.findContours(
        margin_img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    image_segment = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cropped_image = image_array[y:y + h, x:x + w]
        image_segment.append(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY))

    return image_segment


@dask.delayed
def match_template(img_segment, template):
    """
    [summary]

    Parameters
    ----------
    img_segment : list
        list of cropped input image segment
    template : numpy.ndarray
        template image as gray scaled  numpy ndarray

    Returns
    -------
    int
        return flag one if segment match with the template
    """
    # Apply template matching
    template = cv2.resize(template, (2048, 2048))
    res = cv2.matchTemplate(img_segment, template, cv2.TM_CCOEFF_NORMED)
    loc_x, loc_y = np.where(res >= 0.75)
    if len(loc_x) > 0 and len(loc_y) > 0:

        return 1
    return 0
