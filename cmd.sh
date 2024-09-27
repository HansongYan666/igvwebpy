rm -rf /public/workspace/yanhs2024/git/igvwebpy/apps/bamView/static/bams/OC03_A_20240912_RS1-NPNW-40912B-S1-02.bqsr.bam*
samtools view -h -b /public/workspace/yanhs2024/project/Onc_project/14.project/B_analysis/analysis/OC03_A_20240912_RS1-NPNW-40912B-S1-02/aln/OC03_A_20240912_RS1-NPNW-40912B-S1-02.bqsr.bam chr13:32906559-32906569 -o /public/workspace/yanhs2024/git/igvwebpy/apps/bamView/static/bams/OC03_A_20240912_RS1-NPNW-40912B-S1-02.bqsr.bam
samtools index /public/workspace/yanhs2024/git/igvwebpy/apps/bamView/static/bams/OC03_A_20240912_RS1-NPNW-40912B-S1-02.bqsr.bam
