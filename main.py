from train import train, test, ktest, predict
from prandom import throw, xthrow
from os.path import exists
import subprocess
from pickle import dump
import fileInteractions as fi
from printing import printHelp, printSpecificHelp, color, CMD_LIST, printLogo

if not exists('config.pkl'):
    with open('config.pkl', 'wb') as file:
        config = {
            "kernel" : "poly",
            "input_length" : 8,
            "trees_in_the_forest" : 100
        }
        dump(config, file)

print(color.BOLD + "Tài Xỉu Assistant (c)" + color.END)
printLogo()
print("Gõ help để xem danh sách lệnh")
running = True
while (running):
    command = input(">> " + color.BOLD + "@TXA" + color.END + ": " )
    if len(command) == 0:
        continue
    subcommand = command.split()[1:]
    command_name = command.split()[0]
    try:
        if command_name == "help":
            printHelp() if len(subcommand) == 0 else printSpecificHelp(subcommand[0])
        
        elif command_name == "throw":
            throw()

        elif command_name == "xthrow":
            xthrow(int(subcommand[0]), subcommand[1] if len(subcommand) > 1 else "0")

        elif command_name == "test":
            test([int(e) for e in subcommand])

        elif command_name == "ktest":
            ktest("assets/" + (subcommand[0] if subcommand[0] != "default" else "sunwin.txt"), [int(e) for e in subcommand[1:]])
        
        elif command_name == "train":
            train("assets/" + (subcommand[0] if len(subcommand) > 0 else "sunwin.txt"))
        
        elif command_name == "predict":
            predict([int(e) for e in subcommand[1:]], subcommand[0])
        
        elif command_name == "ilength":
            newIL = int(subcommand[0])
            fi.editConfig("input_length", newIL)
            input_length = fi.exportConfig()["input_length"]
            print("Cấu hình thành công. input_length ->", input_length)
        
        elif command_name == "kernel":
            newKernel = subcommand[0]
            if newKernel in ("linear", "poly", "rbf", "sigmoid"):
                fi.editConfig("kernel", newKernel)
                newKernel = fi.exportConfig()["kernel"]
                print("Cấu hình thành công. svr_kernel ->", newKernel)
            else:
                print(f"Kernel {newKernel} không được hỗ trợ")

        elif command_name == "tree":
            newTree = int(subcommand[0])
            fi.editConfig("trees_in_the_forest", newTree)
            print("Cấu hình thành công. trees_in_the_forest ->", newTree)
        
        elif command_name == "config":
            config = fi.exportConfig()
            [print(name, ":", config[name]) for name in config]

        elif command_name == "clear":
            subprocess.run("cls", shell = True)

        elif command_name in ("exit", "quit", "out", "end"):
            running = False
        else:
            print(color.RED + f"Lệnh \"{command_name}\" không tồn tại. Nhập \"help\" để xem danh sách các lệnh khả dụng." + color.END)
    except Exception as error:
        print(color.RED + "Đã xảy ra lỗi. Vui lòng nhập đúng tham số theo mẫu dưới đây hoặc sử dụng \"help <tên_lệnh>\" để biết thêm chi tiết.")
        print("----->",CMD_LIST[command_name]['usage'])
        print("Lỗi:", error, color.END)