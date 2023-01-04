from libs import (
    Flask, render_template, request, jsonify,decode,cv2,imutils,plt
)
from utills import get_filename
from pred_utils import bar_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect',methods=['POST','GET'])
def detect():
    uploaded_file = request.files.get('image')
    incoming_filename = uploaded_file.filename.lower()
    filename = get_filename(incoming_filename)
    local_file = f'static/temp/{filename}'
    uploaded_file.save(local_file)
    image = cv2.imread(local_file)
    actual_img = image
    ratio = image.shape[0] / 500.0
    orig = image.copy()
    image = imutils.resize(image, height = 500)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 75, 200)
    cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
    # loop over the contours
    for c in cnts:
        # approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        # if our approximated contour has four points, then we
        # can assume that we have found our screen
        if len(approx) == 4:
            screenCnt = approx
            break
    # show the contour (outline) of the piece of paper
    try:
        x,y,w,h = cv2.boundingRect(screenCnt)
        croppedImage = image[y-10:y+h+10,x-10:x+w+10]
        local_filename = get_filename("output.png")
        img_loc = f"static/image/{local_filename}"
        plt.imsave(img_loc,cv2.cvtColor(croppedImage,cv2.COLOR_BGR2RGB))
        return jsonify({'filepath':img_loc,'prediction':'','value':''})
    except:
        return jsonify({'filepath':local_file,'prediction':'Not able to detect'})

@app.route('/scan', methods=['POST','GET'])
def scan():

    uploaded_file = request.files.get('image')
    incoming_filename = uploaded_file.filename.lower()
    filename = get_filename(incoming_filename)
    local_file = f'static/temp/{filename}'
    uploaded_file.save(local_file)
    result = bar_detector(local_file,app)
    if result[2]:
        img_b = cv2.imread(result[1])
        val = decode(img_b)
        try:
            res = val[0].data.decode('utf-8')
            res = str(res)
            return jsonify({'filepath':result[0],'prediction':result[1],'value':res})
        except:
            txt = 'Not able to Decode VIN, Please rescan'
            return jsonify({'filepath':result[0],'prediction':result[1],'value':txt})
    else:
        txt = 'Not able to Detect Barcode'
        return jsonify({'filepath':local_file,'prediction':'','value':txt})
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    