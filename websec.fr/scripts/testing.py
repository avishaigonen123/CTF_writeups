import cv2
import pytesseract

def get_captcha(path):

    img = cv2.imread(path)
    h,w=img.shape[:2]

    # cropping borders
    # img = img[5:h-4,5:w-5]

    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # convert from gray to black and white
    bw = cv2.adaptiveThreshold(grayimg, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

    # save converted image
    # cv2.imwrite("captcha_bw.jpg",bw)

    captcha_length = 5 

    # extract text (removes white space and new line)
    cap_data = pytesseract.image_to_string(bw, config='-l eng --oem 1').replace(' ','').replace('\n','')[:captcha_length]

    return cap_data


if __name__ == "__main__":
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--image", help="Captcha image path to solve")
	args = parser.parse_args()

	PATH = "./download.png"
	captcha = get_captcha(PATH)
	print(captcha)