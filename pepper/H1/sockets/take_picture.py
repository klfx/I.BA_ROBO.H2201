from pepper_robots import PepperConfiguration, Robot, PepperNames
import vision_definitions
import paramiko


class Camera:

    __camera_id = vision_definitions.kTopCamera
    __resolution = vision_definitions.kVGA  # 640x480px
    __picture_format = "jpg"

    def __init__(self, robot):
        self.__al_photo = robot.ALPhotoCapture
        self.configure_camera(self.__camera_id, self.__resolution, self.__picture_format)

    def configure_camera(self, camera_id, resolution, format):
        self.__al_photo.setCameraID(camera_id)
        self.__al_photo.setResolution(resolution)
        self.__al_photo.setPictureFormat(format)

    def take_picture(self, path, file_name):
        self.__al_photo.takePicture(path, file_name)


class FileTransfer():

    def __init__(self, robot):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(robot.configuration.Ip, username=robot.configuration.Username, password=robot.configuration.Password)

    def get(self, remote, local):
        sftp = self.ssh.open_sftp()
        sftp.get(remote, local)
        sftp.remove(remote)
        sftp.close()

    def close(self):
        self.ssh.close()


def pepper_spies(robot):
    #config = PepperConfiguration(PepperNames.Ale)
    #robot = Robot(config)
    camera = Camera(robot)

    # take a picture
    robot.ALTextToSpeech.say("taking picture")
    remote_folder_path = "/home/nao/recordings/cameras/"
    file_name = "my_picture.jpg"
    camera.take_picture(remote_folder_path, file_name)

    # copy file to local path
    robot.ALTextToSpeech.say("transfer picture from remote to local")
    local = 'C:\\work\\'+file_name
    remote = remote_folder_path + file_name
    file_transfer = FileTransfer(robot)
    file_transfer.get(remote, local)
    file_transfer.close()
