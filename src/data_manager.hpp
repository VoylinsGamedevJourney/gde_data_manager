#pragma once

#include "godot_cpp/variant/variant.hpp"
#include <godot_cpp/classes/file_access.hpp>
#include <godot_cpp/classes/node.hpp>
#include <godot_cpp/variant/utility_functions.hpp>


using namespace godot;

class DataManager : public Node {
	GDCLASS(DataManager, Node);

private:
public:
	inline void save_data(String a_path) {
		Ref<FileAccess> l_file = FileAccess::open(a_path, FileAccess::WRITE);
		Dictionary l_data = {};
		for (int i = 0; i < get_property_list().size(); i++) {
			int l_usage = get_property_list()[i].get("usage");
			String l_name = get_property_list()[i].get("name");
			if ((l_usage == 4096 || l_usage == 4102) && l_name[0] != '_')
				l_data[l_name] = get(l_name);
		}
		l_file->store_string(UtilityFunctions::var_to_str(l_data));
		l_file->close();
	}

	inline void load_data(String a_path) {
		if (FileAccess::file_exists(a_path)) {
			Ref<FileAccess> l_file = FileAccess::open(a_path, FileAccess::READ);
			Dictionary l_data = UtilityFunctions::str_to_var(l_file->get_as_text());
			Array l_keys = l_data.keys();
			for (int i = 0; i < l_keys.size(); i++) {
				String l_key = l_keys[i];
				set(l_key, l_data[l_key]);
			}
			l_file->close();
		}
	}

protected:
	static inline void _bind_methods() {
		ClassDB::bind_method(D_METHOD("save_data"), &DataManager::save_data);
		ClassDB::bind_method(D_METHOD("load_data"), &DataManager::load_data);
	}
};
