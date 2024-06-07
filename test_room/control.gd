extends Control


func _ready():
	var l_path: String = "res://test.txt"
	var l_test: String = "test failed"
	var l__test: String = "test success"
	var l_export_test: String = "test failed"
	print(Data.test)
	print(Data._test)
	print(Data.export_test)
	Data.save_data(l_path)
	Data.test = l_test
	Data._test = l__test
	Data.export_test = l_export_test
	Data.load_data(l_path)
	print(Data.test)
	print(Data._test)
	print(Data.export_test)
