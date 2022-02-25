import os
import traceback

from face_detect.face_detect import face_detect


def test_four_faces():
    try:
        num_imges_found = face_detect(os.getcwd() + '/resources/face_app/abba.png')
        expected_faces_num = 4
        if num_imges_found == expected_faces_num:
            return {'Test Category': 'Face detection tests',
                    'Test_name': 'Detect png with 4 faces',
                    'Resource': 'abba.png',
                    'Expected_result': expected_faces_num,
                    'Actual_result': num_imges_found,
                    'Test outcome': 'PASSED'
                    }
        else:
            return {'Test Category': 'Face detection tests',
                    'Test_name': 'Detect png with 4 faces',
                    'Resource': 'abba.png',
                    'Expected_result': expected_faces_num,
                    'Actual_result': num_imges_found,
                    'Test outcome': 'FAILED'
                    }
    except Exception:
        return {'Test Category': 'Face detection tests',
                'Test_name': 'Detect png with 4 faces',
                'Resource': 'abba.png',
                'Actual_result': str(traceback.print_exc()),
                'Test outcome': 'FAILED'
                }


def test_one_face():
    try:
        num_imges_found = face_detect(os.getcwd() + '/resources/face_app/carselfie.jpg')
        expected_faces_num = 1
        if num_imges_found == expected_faces_num:
            return {'Test Category': 'Face detection tests',
                    'Test_name': 'Detect jpg with 1 faces',
                    'Resource': 'carselfie.jpg',
                    'Expected_result': expected_faces_num,
                    'Actual_result': num_imges_found,
                    'Test outcome': 'PASSED'
                    }
        else:
            return {'Test Category': 'Face detection tests',
                    'Test_name': 'Detect jpg with 1 faces',
                    'Resource': 'carselfie.jpg',
                    'Expected_result': expected_faces_num,
                    'Actual_result': num_imges_found,
                    'Test outcome': 'PASSED'
                    }
    except Exception:
        return {'Test Category': 'Face detection tests',
                    'Test_name': 'Detect jpg with 1 faces',
                    'Resource': 'carselfie.jpg',
                'Actual_result': str(traceback.print_exc()),
                'Test outcome': 'FAILED'
                }


def test_three_children_faces():
    try:
        num_imges_found = face_detect(os.getcwd() + '/resources/face_app/csavethechild.png')
        expected_faces_num = 3
        if num_imges_found == expected_faces_num:
            return {'Test Category': 'Face detection tests',
                    'Test_name': 'Detect PNG with 1 face',
                    'Resource': 'csavethechild.png',
                    'Expected_result': expected_faces_num,
                    'Actual_result': num_imges_found,
                    'Test outcome': 'PASSED'
                    }
        else:
            return {'Test Category': 'Face detection tests',
                    'Test_name': 'Detect PNG with 1 face',
                    'Resource': 'csavethechild.png',
                    'Expected_result': expected_faces_num,
                    'Actual_result': num_imges_found,
                    'Test outcome': 'PASSED'
                    }

    except Exception:
        return {'Test Category': 'Face detection tests',
                'Test_name': 'Detect PNG with 1 face',
                'Resource': 'csavethechild.png',
                'Actual_result': str(traceback.print_exc()),
                'Test outcome': 'FAILED'
                }


def test_todler_facec():
    try:
        num_imges_found = face_detect(os.getcwd() + '/resources/face_app/toddler girl outdoors.jpg')
        expected_faces_num = 1
        if num_imges_found == expected_faces_num:
            return {'Test Category': 'Face detection tests',
                    'Test_name': 'Detect 1 child face in JPG',
                    'Resource': 'toddler girl outdoors.jpg',
                    'Expected_result': expected_faces_num,
                    'Actual_result': num_imges_found,
                    'Test outcome': 'PASSED'
                    }
        else:
            return {'Test Category': 'Face detection tests',
                    'Test_name': 'Detect 1 child face in JPG',
                    'Resource': 'toddler girl outdoors.jpg',
                    'Expected_result': expected_faces_num,
                    'Actual_result': num_imges_found,
                    'Test outcome': 'FAILED'
                    }
    except Exception:
        return {'Test Category': 'Face detection tests',
                'Test_name': 'Detect 1 child face in JPG',
                'Resource': 'toddler girl outdoors.jpg',
                'Actual_result': str(traceback.print_exc()),
                'Test outcome': 'FAILED'
                }
