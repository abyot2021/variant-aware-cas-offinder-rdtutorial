
How to use the command-line interface
=====================================

Cas-OFFinder is built upon OpenCL to identify potential off-target sites of CRISPR/Cas-derived RNA-guided endonucleases (RGENs).
An OpenCL device is essential for optimal functionality.

Create your environment:

.. code-block:: bash

    conda create -n crispr

Download requirements.txt and vcf-cas-offinder.py from the command-line interface directory and install all dependencies using the command:

.. code-block:: bash

   pip install —no-cache-dir -r requirements.txt

Download the Cas-OFFinder binary file from https://github.com/pnucolab/variant-aware-Cas-OFFinder/blob/main/backend/cas-offinder 
in the same directory with vcf-cas-offinder.py. 

Install the vcflib package using conda, execute the following command:

.. code-block:: bash

   conda install -c bioconda vcflib=1.0.3 tabixpp=1.1.0

Download the chromosome FASTA files for any target organism. You can find one using the links below, or you can use any other sources.

- For Vertebrates

.. code-block:: bash
   
    https://ftp.ensembl.org/pub/
 
- For Plants

 .. code-block:: bash
                
    https://ftp.ensemblgenomes.ebi.ac.uk/pub/plants/

Extract all FASTA files into a directory. Index the extracted reference genome within the same directory

.. code-block:: bash
        
   samtools faidx ref.genome # replace ref.genome with tha actual name of the extracted reference genome 










