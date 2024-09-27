rm -rf /Users/yanhansong/PycharmProjects/igv/apps/bamView/static/bams/T23699.bqsr.bam*
samtools view -h -b /Users/yanhansong/igv/bam/T23699.bqsr.bam chr7:55242462-55242475 -o /Users/yanhansong/PycharmProjects/igv/apps/bamView/static/bams/T23699.bqsr.bam
samtools index /Users/yanhansong/PycharmProjects/igv/apps/bamView/static/bams/T23699.bqsr.bam
