def create_codon_dict(file_path):

    codon_dict = {}  
    with open(file_path, 'r') as file: 
        rows = file.readlines()          

    for row in rows:
        cells = row.strip().split('\t')  
        codon = cells[0]                
        amino_acid = cells[2]            
        codon_dict[codon] = amino_acid  

    return codon_dic
