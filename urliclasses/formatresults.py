class format_result:
    @staticmethod

    def sum_all_results_from_subdomain_fonts(crthsh_results):
        all_results = crthsh_results # + novas listas
        return all_results
    
    def remove_specific_item_from_list(input_list, specific_item):
        return [item for item in input_list if item != specific_item]
        
    def remove_duplicated_items(input_list):
        '''Remove itens duplicados de uma lista, mantendo a ordem original'''
        if len(input_list) != len(set(input_list)):  # Verifica se há duplicados
            return list(set(input_list))  # Remove os duplicados
        else:
            return input_list  # Retorna a lista original se não houver duplicados
