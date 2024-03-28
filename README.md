# Face-recognization-based-attandance-system
Flowchart-  

● For the first time, the admin calls the students to take their pictures to
register them in the database. A new registration cannot be done without
admin permission. Because here it is necessary to enter a password by admin
while registering a new student. 

● Our system takes 100 photo samples for every individual student from different
angles.we have used opencv to take pictures and “viola jones algorithm” to
take faces from the pictures. This algorithm turns physical images into integral
images. This helps to do summation of all pixels in any rectangular box in an
image. In this way we can store each and every individual characteristic of an
image. 

● 100 photo samples for every individual student are then used for training using
Haar Cascade Classifiers where a cascade function is trained from a lot of
images. 

● After that whenever we have to take attendance, the student will come in front of
the camera. It will take the picture of that student and will detect the student with
its details if it is registered in the database. This project uses the Local Binary
Patterns Histograms (LBPH) in OpenCV to perform face recognition.LBP
labels each pixel in an image by comparing the gray level with the neighboring
pixels and then assigning a binary number. It is known for its performance and
how it is able to recognize the face of a person from both the front face and side
face.

● Whenever it detects the student it inserts this record in an excel sheet and shows
it for confirmation.

● We created separate lists for each data column of an entry
● The cascade classifier recognizes multiple faces from the image taken by the
camera
● Our system calculates the confidence value of each face. if it passes the
minimum criteria(say,100) then those entries are recorded in those lists.
● Once all the entries are done, the system just appends the lists using a zip
function.
● So, all attendance is taken in a single computation by our face recognition
system
● We will show the practical implementation of all of these in our upcoming slides.
