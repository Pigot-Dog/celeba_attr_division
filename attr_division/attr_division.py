import shutil
import os
import glob

old_imgs_path = "/home/maxingpei/GAN/Datasets/CelebA-HQ/celeba_hq"
output_imgs_path = "/home/maxingpei/GAN/CycleGAN/code/pytorch-CycleGAN-and-pix2pix/datasets/young2old"

celeba_attr_list_txt = "/home/maxingpei/GAN/Datasets/CelebA-HQ/list_attr_celeba.txt"

attr_index = 40


if __name__ == '__main__':
    trainA_dir = os.path.join(output_imgs_path, "trainA")
    trainB_dir = os.path.join(output_imgs_path, "trainB")
    testA_dir = os.path.join(output_imgs_path, "testA")
    testB_dir = os.path.join(output_imgs_path, "testB")

    if not os.path.isdir(trainA_dir):
        os.makedirs(trainA_dir)
    if not os.path.isdir(trainB_dir):
        os.makedirs(trainB_dir)
    if not os.path.isdir(testA_dir):
        os.makedirs(testA_dir)
    if not os.path.isdir(testB_dir):
        os.makedirs(testB_dir)

    A_train_count = 0
    B_train_count = 0
    A_test_count = 0
    B_test_count = 0

    index = 0
    all_imgs_folders = glob.glob(os.path.join(old_imgs_path, "*"))

    with open(celeba_attr_list_txt, "r") as Attr_list:
        Attr_infos = Attr_list.readlines()
        Attr_infos = Attr_infos[2:]

        for line in Attr_infos:
            infos = line.split()
            filename = infos[0]

            index += 1

            for all_imgs_folder in all_imgs_folders:
                if os.path.isdir(all_imgs_folder):
                    sub_imgs_folders = glob.glob(os.path.join(all_imgs_folder, "*"))
                    for sub_imgs_folder in sub_imgs_folders:
                        # print(os.path.basename(sub_imgs_folder))
                        img_old_path = os.path.join(sub_imgs_folder, filename)
                        if os.path.isfile(img_old_path):

                            try:
                                attr_value = int(infos[attr_index])
                            except IndexError as IE:
                                print(IE)
                                print("now index is {}, the attribute numbers are {}".format(index, len(infos)))
                                print("the infos are {}".format(infos))

                            if attr_value == 1:
                                if os.path.basename(all_imgs_folder) == "train":
                                    img_new_path = os.path.join(output_imgs_path, "trainA", filename)
                                    shutil.copyfile(img_old_path, img_new_path)
                                    A_train_count += 1

                                else:
                                    img_new_path = os.path.join(output_imgs_path, "testA", filename)
                                    shutil.copyfile(img_old_path, img_new_path)
                                    A_test_count += 1

                            else:
                                if os.path.basename(all_imgs_folder) == "train":
                                    img_new_path = os.path.join(output_imgs_path, "trainB", filename)
                                    shutil.copyfile(img_old_path, img_new_path)
                                    B_train_count += 1

                                else:
                                    img_new_path = os.path.join(output_imgs_path, "testB", filename)
                                    shutil.copyfile(img_old_path, img_new_path)
                                    B_test_count += 1

    print("TrainA have %d images!" % A_train_count)
    print("TrainB have %d images!" % B_train_count)
    print("TestA have %d images!" % A_test_count)
    print("TestB have %d images!" % B_test_count)








