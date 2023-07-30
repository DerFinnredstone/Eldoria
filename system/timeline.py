import tkinter as tk
import tkinter.ttk as ttk
from tkinter import simpledialog

class Timeline:
    def __init__(self):
        self.filename = "timeline.txt"
        self.events = []
        self.load_events()
        
        self.root = tk.Tk()
        self.root.title("Timeline")
        
        self.treeview = ttk.Treeview(self.root, columns=("Name", "Year"), show="headings")
        self.treeview.heading("Name", text="Name")
        self.treeview.heading("Year", text="Year")
        self.treeview.pack()
        
        add_button = tk.Button(self.root, text="Add Event", command=self.add_event)
        add_button.pack(side=tk.LEFT)
        
        remove_button = tk.Button(self.root, text="Remove Event", command=self.remove_event)
        remove_button.pack(side=tk.LEFT)
        
        self.display_timeline()
        
        self.root.mainloop()
    
    def load_events(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    event_data = line.strip().split(":")
                    if len(event_data) == 2:
                        name, year = event_data
                        self.events.append((name, year))
        except FileNotFoundError:
            pass
    
    def save_events(self):
        with open(self.filename, 'w') as file:
            for name, year in self.events:
                file.write(f"{name}:{year}\n")
    
    def display_timeline(self):
        self.treeview.delete(*self.treeview.get_children())
        for event in self.events:
            self.treeview.insert("", tk.END, values=event)
    
    def add_event(self):
        name = tk.simpledialog.askstring("Add Event", "Enter the event name:")
        if name:
            year = tk.simpledialog.askstring("Add Event", "Enter the event year:")
            if year:
                self.events.append((name, year))
                self.save_events()
                self.display_timeline()
    
    def remove_event(self):
        selected_item = self.treeview.selection()
        if selected_item:
            item_id = selected_item[0]
            item_values = self.treeview.item(item_id)
            name = item_values['values'][0]
            year = item_values['values'][1]
            self.treeview.delete(item_id)
            self.events = [(n, y) for (n, y) in self.events if n != name or y != year]
            self.save_events()



timeline = Timeline()
