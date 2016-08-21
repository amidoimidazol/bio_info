
#!/usr/bin/perl -w
use strict;
use warnings;

############################################################################################
##################################SUBRUTINE LIB#############################################
############################################################################################

############################################################################################
##################################01 DNS EGYESITES##########################################
############################################################################################

sub egyesit 
	{my ($DNA1 , $DNA2) = @_;
	
	($DNA1 , $DNA2) = ($DNA1 . $DNA2); 
	return $DNA1;
	return $DNA2;
	}
#############################################################################################
###################################02 Nukleotid százalék Adenin##############################
#############################################################################################
sub szazalek_a
		{
	
	my ($DNA) = @_;
	my ($count_a)=0;
	my ($ossz) = length $DNA;
	 ($count_a)= ( $DNA =~ tr/Aa//);
	my ($szazalek) = $count_a/$ossz*100;
	print "ADENIN : $szazalek %\n";
	}
#############################################################################################
###################################03 Nukleotid százalék GUANIN##############################
#############################################################################################

sub szazalek_g
		{
	
	my ($DNA) = @_;
	my ($count_g)=0;
	my ($ossz) = length $DNA;
	 ($count_g)= ( $DNA =~ tr/Gg//);
	my ($szazalek) = $count_g/$ossz*100;
	print "GUANIN : $szazalek %\n";
	}

#############################################################################################
###################################04 Nukleotid százalék CITOZIN#############################
#############################################################################################

sub szazalek_c
		{
	
	my ($DNA) = @_;
	my ($count_a)=0;
	my ($ossz) = length $DNA;
	 ($count_a)= ( $DNA =~ tr/Cc//);
	my ($szazalek) = $count_a/$ossz*100;
	print "CITOZIN : $szazalek %\n";
	}

#############################################################################################
###################################05 Nukleotid százalék TIMIN##############################
#############################################################################################

sub szazalek_t
		{
	
	my ($DNA) = @_;
	my ($count_a)=0;
	my ($ossz) = length $DNA;
	 ($count_a)= ( $DNA =~ tr/Tt//);
	my ($szazalek) = $count_a/$ossz*100;
	print "Timin : $szazalek %\n";
	}
#############################################################################################
###################################07 Nukleotid százalék Osszes##############################
#############################################################################################	

sub szazalek_osszes
		{
	
	my ($DNA) = @_;
	my ($count_a)=0;
	my ($count_g)=0;
	my ($count_c)=0;
	my ($count_t)=0;
	my ($ossz) = length $DNA;
	 ($count_a)= ( $DNA =~ tr/Aa//);
	 ($count_g)= ( $DNA =~ tr/Gg//);
	 ($count_c)= ( $DNA =~ tr/Cc//);
	 ($count_t)= ( $DNA =~ tr/Tt//);
	
	my ($aszazalek) = $count_a/$ossz*100;
	my ($gszazalek) = $count_g/$ossz*100;
	my ($cszazalek) = $count_c/$ossz*100;
	my ($tszazalek) = $count_t/$ossz*100;
	
	print "ADENIN : $aszazalek %\n";
	print "GUANIN : $gszazalek %\n";
	print "CITOZIN : $cszazalek %\n";
	print "TIMIN : $tszazalek %\n";
	}
	
################################################################################################
################################08 Inputra válaszol#############################################
################################################################################################

sub kerdes
	{
	print "Irj be valamit!\n";
	my $i = <STDIN>;
	chomp $i;
	print "es a gep valoszol";
	}
	
#################################################################################################
################################09 CMD line inputre valasz#######################################
#################################################################################################
#közös mappa!
sub help1 
	{
	my ($i) = @_;
	my ($USAGE) = 0;
	
	if ($i =~ /-help/)
		{++$USAGE;}

elsif ($i =~ /-h/)
		{++$USAGE;}

elsif ($i =~ /--help/)
		{++$USAGE;}

else {print "Hiba\n";} 
		
	if ($USAGE>0)
		{$USAGE = print "HELP";}
	}	
#################################################################################################
################################10 HELP##########################################################
#################################################################################################

sub help
	{
	my $i=@_;
	if (1 == 1) 
		{print "DNS szekvencia hossza: -hossz\n
DNS szekvencia bazisainak szazalekos aranya: -szazalek\n
DNS szekvencia bazisainak szama: -szam\n
DNS szekvencia GC telitettseg: -GC\n
Poly T szakasz jelenlete: -polyt\n
Szekvencia kereses: -keres\n
DNS szekvencia megjelenitese: -print\n
Kilepes: -q\n"

				;}}

#################################################################################################
################################11 DNS HOSSZ#####################################################
#################################################################################################


sub hossz {
			my @i = @_;
			my $n = join ('', @i);
			my $t = length($n);
			print "A szekvencia hossza:$t bazispar\n";}


##################################################################################################
###############################12 SZEKVENCIA TISZTITAS############################################
##################################################################################################

sub tisztit {
	my $i = @_;
	
	#whitespace eltuntetese
						$i =~ s/\s//g;
	#kisbetubol nagybetube valtas
						$i =~ tr/agtc/AGTC/;
	
	#szamok eltuntetese					
						my @szamok = ('1','2','3','4','5','6','7','8','9','0'); 	
						$i =~ s/[@szamok]//g;

	}
#################################################################################################
################################13 BAZISOK SZAMA#################################################
#################################################################################################

sub szam
{
my @foo = @_;

my $bar = join ('',@foo);
@foo = split ('',$bar);

my $A = 0;
my $G = 0;
my $C = 0;
my $T = 0;
my $E = 0;
my $base;


foreach  $base (@foo)
	{
	if ($base eq 'A')
		{++$A;}
	elsif ($base eq 'T')
		{++$T;}
	elsif ($base eq 'G')
		{++$G;}
	elsif ($base eq 'C')
		{++$C;}
	else {++$E;}
			}
print "Adenin : $A darab\n";
print "Guanin : $G darab\n";
print "Citozin : $C darab\n";
print "Timin : $A darab\n";
}

#################################################################################################
################################14 GC arany	#####################################################
#################################################################################################


sub GC
{
my @foo = @_;

my $bar = join ('',@foo);
@foo = split ('',$bar);

my $A = 0;
my $G = 0;
my $C = 0;
my $T = 0;
my $E = 0;
my $base;


foreach  $base (@foo)
	{
	if ($base eq 'A')
		{++$A;}
	elsif ($base eq 'T')
		{++$T;}
	elsif ($base eq 'G')
		{++$G;}
	elsif ($base eq 'C')
		{++$C;}
	else {++$E;}
			}

my $ossz = $A + $T + $G + $C;
my $GC = $G + $C;
print ($GC/$ossz*100);
print "% a GC aranya a szekvenciaban!";

}


#################################################################################################
################################15 POLY T KERESES	#############################################
#################################################################################################

sub polyT
	{
	my @i = @_;
	my $n = join ('',@i);
	my $motif = "TTTTT";
	
	if ($n =~ /$motif/)
		{print "\"$motif\" pattern megtalalhato a szekvenciaban, poly T jelen van";}
	else {print "\"$motif\" pattern NEM találhato meg a szekvenciaban, poly T NINCS jelen";}
	}
#################################################################################################
################################16 PATTERN KERESES	#############################################
#################################################################################################
sub keres
	{
	my @i =@_;
	my $n = join ('',@i);
	print "A keresett szekvencia:\n";
	my $motif = <STDIN>;
	chomp $motif;
	
	if ($n =~ /$motif/)
		{print "\"$motif\" szekvencia megtalalhato!";}
	else {print "\"$motif\" szekvencia NEM TALALHATO!";}
	}
		
	
#################################################################################################
################################17 RANDOM POZICIO KIVALASZTASA EGY STRINGBEN	#################
#################################################################################################
# a lehivas elõtt strand (time|$$); kell
sub randomposition
		{
		my($i)=@_;
		
		#visszaadja a randomizalt éréket
		return int(rand(length ($i)));
	}	
#################################################################################################
################################18 RANDOM Nukleotid KIVALASZTASA	#############################
#################################################################################################	
# a lehivas elõtt strand (time|$$); kell

sub randomnucleotid
	{
	my (@i)= ('A', 'G', 'C', 'T');
	
	
	#scalar returns the size of an array.
	# The elements of the array are numbered 0 to size-1
	return randomelem (@i);

	}

#################################################################################################
################################19 RANDOM ELEM KIVALASZTASA EGY STRINGBOL	#####################
#################################################################################################
#random nukleotid az (AGCT)-bõl választ ki egyet úgy hogy átküldi a randomelem subrutinon
#a randomelem subrutin barmire hasznalhato amire rahivjak 

sub randomelem
	{
		my (@n) =@_;
		
		return @n[rand @n];

	}



#################################################################################################
################################20 MUTATE	#####################################################
#################################################################################################
#elõtte seedelni kell a rand-ot! 
#kepes ugyanarra mutalni ( a-rol a-ra mutal)
sub mutate
	{
	my ($dna)=@_;
	my (@nucleotids)= ('A', 'G', 'C', 'T');
	#random pozicio kivalasztasa
	my $position = randomposition ($dna);
	#random nukleotid kivalasztasa (erre mutal)
	my $mutansnukleotid = randomnucleotid (@nucleotids);
	
	# miben --> $dna  hol--> $position mennyit--->1 mire--->$mutansnukleotid
	substr ($dna,$position,1,$mutansnukleotid);
	return $dna;
	}

#################################################################################################
################################21 MUTATE 2.0  ##################################################
#################################################################################################	
#WARNING hasznalat elott seedelni kell a randomot (time|$$)
#Ellenõrzi hogy a mutans ne legyen ugyanaz mint az eredeti nukleotid
# NEMJÓ!!!!!!!!!!!!!!!!!
sub mutate_better
	{
	my ($dna) = @_;
	my (@nucleotids) = ('A', 'G', 'T', 'C');
	#random pozicio kivalasztasa
	my ($position)= randomposition ($dna);
	#elõre ki kell irni mert a bracketben elveszne
	my $mutansnukleotid;
	
	do	
	#a nukleotidokbol kivalaszt egyet random módon
	{ $mutansnukleotid = randomnucleotid (@nucleotids);}
	#amig az kulonbozo nem lesz mint a $dna stringben a random poziciban levo elem
	until ($mutansnukleotid ne substr ($dna, $position,1) );
	
	#kicsereli a $dna-ben $position helyen 1 elemet a $mutansnukleotid stringben levore
	substr ($dna,$position,1,$mutansnukleotid);
	
	return $dna;
	}
	
#################################################################################################
################################22 RANDOM DNS SET GENERALAS  ####################################
#################################################################################################
#	WARNING seedelni kell a randomot elotte 

sub make_random_dna_set
	{
	my ($min_hossz, $max_hossz, $darab)= @_;
	
	my $length;
	my $dna;
	my @set;
	
	#annyiszor loopol ahany dns darabot akarunk
	for (my $i = 0; $i < $darab;++$i)
		
		{
		#randomhossz meghatarozasa atkuldes masik subrutinba
		$length = randomlength ($min_hossz,$max_hossz);
		
		#random dna subrutinba kuldi a randomhossz erteket
		$dna = make_random_dna ($length);
		
		# $dna elemeit a @set-hez adja
		push (@set, $dna);
		}
		
		return @set;
		}


#################################################################################################
################################23 RANDOM HOSSZ  ################################################
#################################################################################################
sub randomlength
	{
	my ($min,$max)=@_;
	
	# +1 mindenkepp kell ez a formula hasznalhato hogy a ket ertek között levo szamokbol valasszon egyet random, visszakuldi 
	return (int(rand($max-$min+1))+$min);
	
	}
	
#################################################################################################
################################23 RANDOM DNS LEGENERALAS  ######################################
#################################################################################################	
sub make_random_dna
	{
	my ($length) = @_;
	
	my $dna;
	
	#addig megy mig a kivant hosszt el nem eri
	for (my $i=0; $i<$length;++$i)
			
			#lefuttatja a randomnucleotid subrutint és az igy generalt karakter hozzadja a stringhez (.=)
			{$dna .= randomnucleotid ( );}
			
	return $dna;
	}
			

#################################################################################################
################################24 HASONLO ARANY  ###############################################
#################################################################################################

sub matching_percentage
	{
	my($string1, $string2) = @_;
	
	my ($length) = length ($string1);
	my $position;
	my ($count) = 0;
	
	for ($position=0; $position < $length ; ++$position)
	{
		if(substr($string1,$position,1)	eq substr($string2,$position,1))
				{++$count;}
	}
	return $count/ $length;
	}
		
	
#################################################################################################
################################25 SHUFFLE  #####################################################
#################################################################################################

sub everydayimshufflin
	{
#	my (@a) = @_;
	
#	my @set;
#	my $t;
#	my $voltmar;
#	my @n;
#	my $length = scalar (@a);
	

#do		
#		{
	
			
#			if (@n  ne 15)
#			{
#			$t = int(rand($length));
#			$voltmar .= $t;
#			@n = @a[$t,($t+1)];
		
#		push (@set , @n);
#		}
		
#		while (scalar @set < $length);
#		return @set;
#		}
#}

#sub everydayimshufflin2
#	{
#	my (@a) = @_;
#	my ($a) = join (''.@a);
#	my $length = scalar (@a);
#	my $foo;
#	my $bar;
#	my @bar;
#	my @set;
#	my $t;
#	do
#		{
#		$t = int(rand($length));
		
#		$a = @a[$t,($t+1)];
#		$foo .= $a;
		
#						if (substr($foo) ne /$bar/)
#									{
#									@bar = @a[$t,($t+1)];
#									push (@set , @bar);
#									}	
	
#	while (scalar @set < $length);
#		return @set;
#		}}

#sub everydayimshufflin3
#	{
#	my $a = @_;
#	my $length = length $a;
	
	#randompozicio
#	my $randomelem = randomelem ($a);
	}
	############################################################################
	##########################26 Codon mutator###################################
	############################################################################
	
	
#beirsz egy kodont 3 nukleotid
# random mutaciot csinal

sub codonmutans
	{
my @codon = @_;
my $n = join ('',@codon);
my $mutatedcodon = mutate_better($n);

return $mutatedcodon;
}

############################################################################
#############################27 PROTEIN MUTATOR###########################
############################################################################

sub mutate_protein
	{
	my (@protein) = @_;
	my $protein = join ('',@protein);
	my (@amino_acid) = ('R','H','K','D','E','S','T','N','Q','C','U','G','P','A','V','I','L','M','F','Y','W');
	my $mutant;
	my $i = 0;

					my $position = randomposition ($protein);
		do
		
		{$mutant = randomelem (@amino_acid);}
		
		until ($mutant ne substr ($protein, $position, 1));
		
		substr ($protein,$position,1,$mutant);
		
		
		return $protein;
		}
		

############################################################################
#############################28 KODON AS##################################
############################################################################
sub codon_as1 {
my($codon) = @_;
if ( $codon =~ /TCA/i ) { return 'S' } #

elsif ( $codon =~ /TCC/i ) { return 'S' } #

elsif ( $codon =~ /TCG/i ) { return 'S' } #

elsif ( $codon =~ /TCT/i ) { return 'S' } #

elsif ( $codon =~ /TTC/i ) { return 'F' } #

elsif ( $codon =~ /TTT/i ) { return 'F' } #

elsif ( $codon =~ /TTA/i ) { return 'L' } #

elsif ( $codon =~ /TTG/i ) { return 'L' } #

elsif ( $codon =~ /TAC/i ) { return 'Y' } #

elsif ( $codon =~ /TAT/i ) { return 'Y' } #

elsif ( $codon =~ /TAA/i ) { return '_' } # Stop
elsif ( $codon =~ /TAG/i ) { return '_' } # Stop
elsif ( $codon =~ /TGC/i ) { return 'C' } #

elsif ( $codon =~ /TGT/i ) { return 'C' } #

elsif ( $codon =~ /TGA/i ) { return '_' } # Stop
elsif ( $codon =~ /TGG/i ) { return 'W' } #

elsif ( $codon =~ /CTA/i ) { return 'L' } #

elsif ( $codon =~ /CTC/i ) { return 'L' } #

elsif ( $codon =~ /CTG/i ) { return 'L' } #

elsif ( $codon =~ /CTT/i ) { return 'L' } #

elsif ( $codon =~ /CCA/i ) { return 'P' } #

elsif ( $codon =~ /CCC/i ) { return 'P' } #

elsif ( $codon =~ /CCG/i ) { return 'P' } #

elsif ( $codon =~ /CCT/i ) { return 'P' } #

elsif ( $codon =~ /CAC/i ) { return 'H' } #

elsif ( $codon =~ /CAT/i ) { return 'H' } #

elsif ( $codon =~ /CAA/i ) { return 'Q' } #

elsif ( $codon =~ /CAG/i ) { return 'Q' } #

elsif ( $codon =~ /CGA/i ) { return 'R' } #

elsif ( $codon =~ /CGC/i ) { return 'R' } #

elsif ( $codon =~ /CGG/i ) { return 'R' } #

elsif ( $codon =~ /CGT/i ) { return 'R' } #

elsif ( $codon =~ /ATA/i ) { return 'I' } #

elsif ( $codon =~ /ATC/i ) { return 'I' } #

elsif ( $codon =~ /ATT/i ) { return 'I' } #

elsif ( $codon =~ /ATG/i ) { return 'M' } #

elsif ( $codon =~ /ACA/i ) { return 'T' } #

elsif ( $codon =~ /ACC/i ) { return 'T' } #

elsif ( $codon =~ /ACG/i ) { return 'T' } #

elsif ( $codon =~ /ACT/i ) { return 'T' } #

elsif ( $codon =~ /AAC/i ) { return 'N' } #

elsif ( $codon =~ /AAT/i ) { return 'N' } #

elsif ( $codon =~ /AAA/i ) { return 'K' } #

elsif ( $codon =~ /AAG/i ) { return 'K' } #

elsif ( $codon =~ /AGC/i ) { return 'S' } #

elsif ( $codon =~ /AGT/i ) { return 'S' } #

elsif ( $codon =~ /AGA/i ) { return 'R' } #

elsif ( $codon =~ /AGG/i ) { return 'R' } #

elsif ( $codon =~ /GTA/i ) { return 'V' } #

elsif ( $codon =~ /GTC/i ) { return 'V' } #

elsif ( $codon =~ /GTG/i ) { return 'V' } #

elsif ( $codon =~ /GTT/i ) { return 'V' } #

elsif ( $codon =~ /GCA/i ) { return 'A' } #

elsif ( $codon =~ /GCC/i ) { return 'A' } #

elsif ( $codon =~ /GCG/i ) { return 'A' } #

elsif ( $codon =~ /GCT/i ) { return 'A' } #

elsif ( $codon =~ /GAC/i ) { return 'D' } #

elsif ( $codon =~ /GAT/i ) { return 'D' } #

elsif ( $codon =~ /GAA/i ) { return 'E' } #

elsif ( $codon =~ /GAG/i ) { return 'E' } #

elsif ( $codon =~ /GGA/i ) { return 'G' } #

elsif ( $codon =~ /GGC/i ) { return 'G' } #

elsif ( $codon =~ /GGG/i ) { return 'G' } #

elsif ( $codon =~ /GGT/i ) { return 'G' } #

else {
print STDERR "Bad codon \"$codon\"!!\n"; #STDERR olyan mint az STDIN  de egy kulon file-ba kuldi a printet (error gyujtesre jo)
exit;
}
}



############################VERSION 2 ######################################
# Version 2
sub codon_as2 {
my($codon) = @_;
if ( $codon =~ /GC./i) { return 'A' } 

elsif ( $codon =~ /TG[TC]/i) { return 'C' } #A harmadik elem lehet T VAGY C

elsif ( $codon =~ /GA[TC]/i) { return 'D' } 

elsif ( $codon =~ /GA[AG]/i) { return 'E' } #

elsif ( $codon =~ /TT[TC]/i) { return 'F' } #

elsif ( $codon =~ /GG./i) { return 'G' } # A harmadik elem bármi lehet AGCT

elsif ( $codon =~ /CA[TC]/i) { return 'H' } #

elsif ( $codon =~ /AT[TCA]/i) { return 'I' } #

elsif ( $codon =~ /AA[AG]/i) { return 'K' } #

elsif ( $codon =~ /TT[AG]|CT./i) { return 'L' } # TT + A vagy G és lehet (|) CT és bármi (.)

elsif ( $codon =~ /ATG/i) { return 'M' } #

elsif ( $codon =~ /AA[TC]/i) { return 'N' } #

elsif ( $codon =~ /CC./i) { return 'P' } #

elsif ( $codon =~ /CA[AG]/i) { return 'Q' } #

elsif ( $codon =~ /CG.|AG[AG]/i) { return 'R' } #

elsif ( $codon =~ /TC.|AG[TC]/i) { return 'S' } #

elsif ( $codon =~ /AC./i) { return 'T' } #

elsif ( $codon =~ /GT./i) { return 'V' } #

elsif ( $codon =~ /TGG/i) { return 'W' } #

elsif ( $codon =~ /TA[TC]/i) { return 'Y' } #

elsif ( $codon =~ /TA[AG]|TGA/i) { return '_' } #

else {
print STDERR "Bad codon \"$codon\"!!\n";
exit;
}
}
###################################HASH VERSION####################################


#
# codon2aa
#
# A subroutine to translate a DNA 3-character codon to an

# Version 3, using hash lookup
sub codon_as3 {
my ($codon) = @_;
$codon = uc $codon; # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! uc caracther sensitiv tehát nemkell feltétlen kis / nagy betunke lennie
my(%genetic_code) = (
'TCA' => 'S', # Serine
'TCC' => 'S', # Serine
'TCG' => 'S', # Serine
'TCT' => 'S', # Serine
'TTC' => 'F', # Phenylalanine
'TTT' => 'F', # Phenylalanine
'TTA' => 'L', # Leucine
'TTG' => 'L', # Leucine
'TAC' => 'Y', # Tyrosine
'TAT' => 'Y', # Tyrosine
'TAA' => '_', # Stop
'TAG' => '_', # Stop
'TGC' => 'C', # Cysteine
'TGT' => 'C', # Cysteine
'TGA' => '_', # Stop
'TGG' => 'W', # Tryptophan
'CTA' => 'L', # Leucine
'CTC' => 'L', # Leucine
'CTG' => 'L', # Leucine
'CTT' => 'L', # Leucine
'CCA' => 'P', # Proline
'CCC' => 'P', # Proline
'CCG' => 'P', # Proline
'CCT' => 'P', # Proline
'CAC' => 'H', # Histidine
'CAT' => 'H', # Histidine
'CAA' => 'Q', # Glutamine
'CAG' => 'Q', # Glutamine
'CGA' => 'R', # Arginine
'CGC' => 'R', # Arginine
'CGG' => 'R', # Arginine
'CGT' => 'R', # Arginine
'ATA' => 'I', # Isoleucine
'ATC' => 'I', # Isoleucine
'ATT' => 'I', # Isoleucine
'ATG' => 'M', # Methionine
'ACA' => 'T', # Threonine
'ACC' => 'T', # Threonine
'ACG' => 'T', # Threonine
'ACT' => 'T', # Threonine
'AAC' => 'N', # Asparagine
'AAT' => 'N', # Asparagine
'AAA' => 'K', # Lysine
'AAG' => 'K', # Lysine
'AGC' => 'S', # Serine
'AGT' => 'S', # Serine
'AGA' => 'R', # Arginine
'AGG' => 'R', # Arginine
'GTA' => 'V', # Valine
'GTC' => 'V', # Valine
'GTG' => 'V', # Valine
'GTT' => 'V', # Valine
'GCA' => 'A', # Alanine
'GCC' => 'A', # Alanine
'GCG' => 'A', # Alanine
'GCT' => 'A', # Alanine
'GAC' => 'D', # Aspartic Acid
'GAT' => 'D', # Aspartic Acid
'GAA' => 'E', # Glutamic Acid
'GAG' => 'E', # Glutamic Acid
'GGA' => 'G', # Glycine
'GGC' => 'G', # Glycine
'GGG' => 'G', # Glycine
'GGT' => 'G', # Glycine
);
if(exists $genetic_code{$codon}) { #exist = ha létezik a file )
return $genetic_code{$codon};
}else{
print STDERR "Bad codon \"$codon\"!!\n";
exit;
}
}


#############################################################################
#########################29 DNS --> FEH ######################################
#############################################################################

sub dna2peptide {
my($dna) = @_;


my $protein = '';
for(my $i=0; $i < (length($dna) - 2) ; $i += 3) {
$protein .= codon_as2( substr($dna,$i,3) );
}
return $protein;
}


#############################################################################
#########################30 GET FILE DATA ####################################
#############################################################################

# get_file_data
#
# A subroutine to get data from a file given its filename
sub get_file_data {
my($filename) = @_;

my @filedata = ( );
unless( open(GET_FILE_DATA, $filename) ) 
		{print STDERR "Cannot open file \"$filename\"\n\n";
		exit;}

@filedata = <GET_FILE_DATA>;
close GET_FILE_DATA;
return @filedata;
}

#############################################################################
#########################31 GET SEQUENCE ##################################
#############################################################################

# extract_sequence_from_fasta_data
#
# A subroutine to extract FASTA sequence data from an array
sub get_sequence {
my(@fasta_file_data) = @_;

# Declare and initialize variables
my $sequence = '';

foreach my $line (@fasta_file_data) {
# discard blank line
if ($line =~ /^\s*$/) {
next;
# discard comment line
} elsif($line =~ /^\s*#/) {
next;
# discard fasta header line
} elsif($line =~ /^>/) {
next;
# keep line, add to sequence string
} else {
$sequence .= $line;
}
}
# remove non-sequence data (in this case, whitespace)
#from $sequence string
$sequence =~ s/\s//g;
return $sequence;
}

#############################################################################
#########################32 Print Sequence ####################################
#############################################################################
# print_sequence
#
# A subroutine to format and print sequence data

sub print_sequence {
my($sequence, $length) = @_;

# Print sequence in lines of $length
for ( my $pos = 0 ; $pos < length($sequence) ; $pos +=
$length ) {
print substr($sequence, $pos, $length), "\n";
}
}

#############################################################################
#########################33 Reverse complement ################################
#############################################################################
# revcom
#
# A subroutine to compute the reverse complement of DNA


sub revcom {
my($dna) = @_;
# First reverse the sequence
my($revcom) = reverse($dna);
# Next, complement the sequence, dealing with upper and

# A->T, T->A, C->G, G->C
$revcom =~ tr/ACGTacgt/TGCAtgca/;
return $revcom;
}

###########################################################################
#########################34 FRAMESHIFT####################################
###########################################################################

# translate_frame
#
# A subroutine to translate a frame of DNA
sub translate_frame {
my($seq, $start, $end) = @_;
my $protein;

# To make the subroutine easier to use, you won't need
#to specify
# the end point--it will just go to the end of the
#sequence
# by default.
unless($end) 
	{$end = length($seq);}
# Finally, calculate and return the translation
return dna2peptide ( substr ( $seq, $start - 1,
$end -$start + 1) );
}



































1;