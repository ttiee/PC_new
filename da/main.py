from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel, QFormLayout, QFileDialog, QMessageBox
import sys
import os
import py7zr
import wget


class MainWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 以下三个变量可以不需要，可以用QLabel的值代替
        self.image = ''
        self.cacheDir = ''
        self.setupDisk = ''

        self.home = QFormLayout(self)
        self.selectImageButton = QPushButton('选择镜像', self)
        self.selectImageLabel = QLabel(self)
        self.selectCacheDirButton = QPushButton('选择缓存目录', self)
        self.selectCacheLabel = QLabel(self)
        self.selectSetupDiskButton = QPushButton('选择安装磁盘', self)
        self.selectSetupDiskLabel = QLabel(self)
        self.runButton = QPushButton('运行', self)
        self.init_ui()

    def init_ui(self):
        self.setMinimumSize(800, 500)
        self.selectImageButton.clicked.connect(self.select_image)
        self.selectCacheDirButton.clicked.connect(self.select_cache_dir)
        self.selectSetupDiskButton.clicked.connect(self.select_setup_disk)
        self.runButton.clicked.connect(self.run)
        self.home.addRow(self.selectImageButton, self.selectImageLabel)
        self.home.addRow(self.selectCacheDirButton, self.selectCacheLabel)
        self.home.addRow(self.selectSetupDiskButton, self.selectSetupDiskLabel)
        self.home.addRow(self.runButton)
        self.show()

    def select_image(self):
        imagefile = QFileDialog.getOpenFileName(self, '打开镜像', '', '镜像文件 (*.bugdowsimage)')[0]
        if imagefile:
            self.selectImageLabel.setText(imagefile)
            self.image = imagefile

    def select_cache_dir(self):
        Cachedrive = QFileDialog.getExistingDirectory(self, '选择缓存目录打开镜像', '')
        if Cachedrive:
            self.selectCacheLabel.setText(Cachedrive)
            self.cacheDir = Cachedrive

    def select_setup_disk(self):
        installdisk = QFileDialog.getExistingDirectory(self, '选择安装盘', '')
        if installdisk:
            self.selectSetupDiskLabel.setText(installdisk)
            self.setupDisk = ''

    def run(self):
        lacks = []  # 附送的检查参数完整代码
        if not self.cacheDir:
            lacks.append('缓存目录')
        if not self.image:
            lacks.append('镜像')
        if not self.setupDisk:
            lacks.append('安装磁盘')
        if lacks:
            QMessageBox.warning(self,
                                '参数不足',
                                ', '.join(lacks) + '未添加\n请添加',
                                QMessageBox.StandardButton.Ok,
                                QMessageBox.StandardButton.Ok)
        else:
            # 定义变量
            Cache = Cachedrive + '\Bugdows Install Cache'
            winverfile = Cache + '\winver.bugdowskey'
            yanzheng = Cache + '\yz.bugdowsyz'
            # 创建文件夹
            print("创建文件夹<=")
            os.makedirs('Cache', exist_ok=True)
            print("创建文件夹 【OK】")
            # 组装字符串
            authsite = 'https://auth.easysys.top/' + winver + '/key.bugdowskey'
            fileimg = Cache + '\Bugdows image.wim'

            # 解压文件
            print("解压镜像<=")
            archive = py7zr.SevenZipFile('imagefile', mode='r')
            archive.extractall(path="Cache")
            archive.close()
            print("解压镜像【OK】")
            # 下载文件
            print("下载密钥<=")
            wget.download(authsite, Cache)
            print("下载密钥【OK】")
            # 打开文件
            print("对比文件<=")
            file = open("winver", "r")
            winver = file.read(10)
            file.close()
            file = open("yanzheng", "r")
            yz = file.read(1)
            file.close()
            # 验证字符串
            if not yz == 'y':
                QMessageBox.information(self, "提示", "此镜像不被支持",
                                        QMessageBox.Yes)
            print("对比文件【OK】")
            print("验证部分已完成，进入部署部分")
            print("部署<=")
            os.system('imagex.exe /apply fileimg 1 installdisk verify')
            print("部署【OK】")
            QMessageBox.information(self, "提示", "部署完成！",
                                    QMessageBox.Yes)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWidget = MainWidget()
    sys.exit(app.exec())
