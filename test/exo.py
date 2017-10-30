FichierEntree = open("ex-2.pkl", "r"); # Ouverture du fichier en lecture
FichierSortie = open("FichierSortie.mgf", "w"); # Ouverture du fichier en ecriture
#lignes = FichierEntree.read();
lignes = FichierEntree.readlines();
FichierEntree.close();
FichierSortie.write("COM=\nCHARGE=\n");
nbligne = 0;
for ligne in lignes:
	if ligne == '\n':
		nbligne += 1;
		valPEPMASS = 352; # à titre indicatif
		FichierSortie.write("\nBEGIN IONS\nTITLE=ex-2.pkl."+str(nbligne-1)+"\nPEPMASS="+str(valPEPMASS)+"\nCHARGE="+str(nbligne)+"+\n");
	else:
		FichierSortie.write(ligne);
	pass
FichierSortie.close();