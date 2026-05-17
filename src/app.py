#!/usr/bin/env python3
"""
XML格式化工具 - 美化/压缩/校验XML
"""
import sys, tkinter as tk
from tkinter import messagebox, scrolledtext
import tkinter as tk
import xml.dom.minidom as minidom

class App:
    def __init__(self, root):
        self.root = root
        root.title("XML格式化工具 v1.0")
        root.geometry("800x600")
        self.build_ui()
    
    def build_ui(self):
        f = tk.Frame(self.root, bg="#e65100", height=50)
        f.pack(fill="x")
        tk.Label(f, text="📑 XML格式化工具", font=("Arial",14,"bold"),
                 fg="white", bg="#e65100").pack(pady=12)
        
        main = tk.Frame(self.root, padx=15, pady=10)
        main.pack(fill="both", expand=True)
        
        bf = tk.Frame(main)
        bf.pack(fill="x", pady=5)
        tk.Button(bf, text="格式化（美化）", command=self.format_xml,
                  bg="#e65100", fg="white", padx=15).pack(side="left", padx=5)
        tk.Button(bf, text="压缩（一行）", command=self.compress_xml,
                  padx=15).pack(side="left", padx=5)
        tk.Button(bf, text="校验XML", command=self.validate_xml,
                  bg="#4caf50", fg="white", padx=15).pack(side="left", padx=5)
        tk.Button(bf, text="复制结果", command=self.copy_result,
                  bg="#ff9800", fg="white", padx=15).pack(side="left", padx=5)
        tk.Button(bf, text="清空", command=self.clear,
                  bg="#d9534f", fg="white", padx=15).pack(side="right", padx=5)
        
        tk.Label(main, text="输入XML：", font=("Arial",10,"bold")).pack(anchor="w")
        self.input_txt = scrolledtext.ScrolledText(main, font=("Consolas",10),
                                                    height=12, wrap="none")
        self.input_txt.pack(fill="both", expand=True, pady=5)
        
        tk.Label(main, text="输出结果：", font=("Arial",10,"bold")).pack(anchor="w", pady=(10,0))
        self.output_txt = scrolledtext.ScrolledText(main, font=("Consolas",10),
                                                     height=12, wrap="none",
                                                     bg="#f5f5f5")
        self.output_txt.pack(fill="both", expand=True, pady=5)
        
        self.status = tk.Label(main, text="粘贴XML后点击「格式化」",
                               font=("Arial",10), fg="gray")
        self.status.pack(anchor="w")
    
    def get_input(self):
        return self.input_txt.get(1.0, "end").strip()
    
    def set_output(self, text):
        self.output_txt.delete(1.0, "end")
        self.output_txt.insert(1.0, text)
    
    def format_xml(self):
        try:
            dom = minidom.parseString(self.get_input())
            result = dom.toprettyxml(indent="  ")
            # 移除空行
            lines = [l for l in result.split("\n") if l.strip()]
            self.set_output("\n".join(lines))
            self.status.config(text="✅ 格式化成功")
        except Exception as e:
            messagebox.showerror("XML错误", f"无效的XML：\n{str(e)}")
    
    def compress_xml(self):
        try:
            dom = minidom.parseString(self.get_input())
            result = dom.toxml()
            self.set_output(result)
            self.status.config(text=f"✅ 压缩成功")
        except Exception as e:
            messagebox.showerror("XML错误", f"无效的XML：\n{str(e)}")
    
    def validate_xml(self):
        try:
            minidom.parseString(self.get_input())
            messagebox.showinfo("校验结果", "✅ XML格式正确！")
            self.status.config(text="✅ XML有效")
        except Exception as e:
            messagebox.showerror("校验失败", f"❌ XML格式错误：\n{str(e)}")
    
    def copy_result(self):
        text = self.output_txt.get(1.0, "end")
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        messagebox.showinfo("复制成功", "结果已复制到剪贴板")
    
    def clear(self):
        self.input_txt.delete(1.0, "end")
        self.output_txt.delete(1.0, "end")
        self.status.config(text="已清空")

if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
