def create_codon_dict(file_path):

    codon_dict = {}  # מילון ריק
    with open(file_path, 'r') as file:  # פותחים את הקובץ
        rows = file.readlines()          # קוראים את כל השורות

    for row in rows:
        cells = row.strip().split('\t')  # מסירים רווחים ו-\n ומפרקים לפי טאבים
        codon = cells[0]                 # הקודון הוא התא הראשון
        amino_acid = cells[2]            # הקיצור של חומצת האמינו הוא התא השלישי
        codon_dict[codon] = amino_acid   # מוסיפים למילון

  return codon_dict
