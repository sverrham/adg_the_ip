
orderable = {"a": "Champagne", "b": "box of chocolate", "c": "bag of chocolate", "d": "some surprise"}


class OrderSystem:

	def __init__(self):
		self.input = ""
		self.ordered = False
		self.done = False

	def process(self, data):
		#Make this simple.
		#add until new line
		if self.done:
			return ""
		if "\n" not in data :
			self.input += data
			return ""
		if len(data) > 1:
			self.input += data.strip()

		#We have \n input here so a new line and the input should be completed lets process and reply.
		print(self.input)
		if self.input in orderable:
			self.ordered = True
			self.item = self.input
			input_ordered = self.input
			self.input = ""
			return "\r\nyou want {}, to where and whom should it be delivered?\r\n".format(input_ordered)
		else:
			if self.ordered:
				ordered_item_to_team = "{} ordered to team {} thank you for participating and the item is maybe beeing processed, (ps send sverre a slack message to speed it up)\r\n".format(self.item, self.input)
				print (ordered_item_to_team)
				
				self.input = ""
				self.ordered = False
				self.done = True
				return ordered_item_to_team
			else:
				#Wrong inputs, so lets send the shoping list.
				shoping_list = "\r\nWe sell we deal, here you can ordere what you want and what you need, but only 1 per team:\r\n"
				for key,value in orderable.items():
					shoping_list += "{}:{}\r\n".format(key, value)
					
				self.input = ""
				return shoping_list	

		print("ERROR,ERROR,ERROR")