class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

CMD_LIST = {
    "throw" : {
        "description" : "Tung 3 xúc xắc một cách ngẫu nhiên, nhận từng giá trị và tổng của chúng.",
        "usage" : "throw",
        "args" : None
    },
    "xthrow" : {
        "description" : "Tung 3 xúc xắc một số lần nhất định, nhận lại thống kê kết quả.",
        "usage" : "throw [iteration] [analysis]",
        "args" : {
            "iteration" : {
                "dtype" : "int",
                "note" : "Cần là một số tự nhiên",
                "default" : "Không"
            },
            "analysis" : {
                "dtype" : "str",
                "note" : "Nhập 1 để nhận phân tích chi tiết. Mọi giá trị khác sẽ chỉ trả về kết quả",    
                "default" : "0"
            }
        }
    },
    "train" : {
        "description" : "Huấn luyện các mẫu học máy từ file dữ liệu chỉ định",
        "usage" : "train [file_location]",
        "args" : {
            "file_location" : {
                "dtype" : "str",
                "note" : "Là tên một file .txt được chứa trong thư mục /assets",
                "default" : "sunwin.txt"
            }
        }
    },
    "test" : {
        "description" : "Kiểm tra độ chính xác của từng mẫu học máy trong phiên chỉ định",
        "usage" : "test [data]",
        "args" : {
            "data" : {
                "dtype" : "*int",
                "note" : "Độ dài của mẫu kiểm thử cần lớn hơn input_length ít nhất là 3",
                "default" : "Không"
            }
        }
    },
    "ktest" : {
        "description" : "Kiểm tra độ chính xác của từng kernel SVR được huấn luyện theo file dữ liệu chỉ định,",
        "usage" : "test [file_location] [data]",
        "args" : {
            "file_location" : {
                "dtype" : "str",
                "note" : "Là tên một file .txt được chứa trong thư mục /assets",
                "default" : "sunwin.txt"
            },
            "data" : {
                "dtype" : "*int",
                "note" : "Độ dài của mẫu kiểm thử cần lớn hơn input_length ít nhất là 3",
                "default" : "Không"
            }
        }
    },
    "predict" : {
        "description" : "Dự đoán kết quả lượt tiếp theo từ dữ liệu phiên chỉ định",
        "usage" : "predict [model] [data]",
        "args" : {
            "model" : {
                "dtype" : "all | svr | rf | nn",
                "note" : "Không",
                "default" : "Không"
            },
            "data" : {
                "dtype" : "*int",
                "note" : "Độ dài của mẫu đầu vào cần bằng chính xác input_length",
                "default" : "Không"
            }
        }
    },
    "config" : {
        "description" : "Xem các cấu hình hiện tại",
        "usage" : "config",
        "args" : None
    },
    "ilength" : {
        "description" : "Điều chỉnh độ dài chuỗi đầu yêu cầu vào trong file cấu hình",
        "usage" : "ilength [length]",
        "args" : {
            "length" : {
                "dtype" : "int",
                "note" : "Là một số tự nhiên lớn hơn 0. Không nên điều chỉnh nếu không hiểu rõ. Sau khi điều chỉnh cần huấn luyện lại model",
                "default" : "8"
            }
        }
    },
    "kernel" : {
        "description" : "Tùy chọn kernel cho thuật toán SVR trong file cấu hình.",
        "usage" : "kernel [ker]",
        "args" : {
            "ker" : {
                "dtype" : "linear | poly | rbf | sigmoid",
                "note" : "Không nên điều chỉnh nếu không hiểu rõ. Sau khi chỉnh cần huấn luyện lại model để cập nhật kernel.",
                "default" : "poly"
            }
        }
    },
    "tree" : {
        "description" : "Tùy chọn số lượng cây cho thuật toán Random Forest trong file cấu hình.",
        "usage" : "tree [quantity]",
        "args" : {
            "tree" : {
                "dtype" : "int",
                "note" : "Là một số lớn hơn 0. Không nên điều chỉnh nếu không hiểu rõ. Sau khi chỉnh cần huấn luyện lại model.",
                "default" : "100"
            }
        }
    },
}

def printLogo():
    print(color.GREEN + """'########:'##::::'##::::'###::::
... ##..::. ##::'##::::'## ##:::
::: ##:::::. ##'##::::'##:. ##::
::: ##::::::. ###::::'##:::. ##:
::: ##:::::: ## ##::: #########:
::: ##::::: ##:. ##:: ##.... ##:
::: ##:::: ##:::. ##: ##:::: ##:
:::..:::::..:::::..::..:::::..::""" + color.END)

def printHelp():
    print(color.BOLD + "Các lệnh khả dụng (sử dụng \"help <tên_lệnh>\" để xem thông tin chi tiết):" + color.END)
    for command in CMD_LIST:
        print(f"- {color.YELLOW + command + color.END}\n    \__{CMD_LIST[command]['description']}\n")

def printSpecificHelp(command_name):
    if command_name in CMD_LIST:
        print(color.YELLOW + "Mô tả:" + color.END)
        print(CMD_LIST[command_name]["description"] + "\n")
        print(color.YELLOW + "Sử dụng:" + color.END)
        print(CMD_LIST[command_name]["usage"] + "\n")
        if CMD_LIST[command_name]["args"] == None:
            return
        print(color.YELLOW + "Tham số:" + color.END)
        for arg in CMD_LIST[command_name]['args']:
            argd = CMD_LIST[command_name]['args'][arg]
            print(f"{color.GREEN + arg + color.END} -> {color.CYAN + argd['dtype'] + color.END}")
            print(f"\t{color.BOLD}Lưu ý{color.END}: {argd['note']}")
            print(f"\tGiá trị mặc định: {argd['default']}") if argd['default'] != "Không" else None
    else:
        print(color.RED + f"Lệnh \"{command_name}\" không tồn tại. Nhập \"help\" để xem danh sách các lệnh khả dụng." + color.END)