from django.shortcuts import render
from pathlib import Path
# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os,json
from django.conf import settings
import pysam
from subprocess import run


def index(request):
    return render(request, 'index.html')

def releasebampath():
    sampledir = settings.BAM_PATH
    outfile = settings.BAM_PATH_FILE
    out = open(outfile,"w")
    for indir in sampledir:
        for bamfile in Path(indir).rglob("*.bqsr.bam"):
            out.write(str(bamfile)+ "\n")
    out.close()

def get_bam(request):
    samtools = settings.SAMTOOLS
    if request.method == "POST":
        data = json.loads(request.body)
        bamFile = data['bamFile']
        if not os.path.exists(bamFile):
            releasebampath()
            bamFile = os.popen(f"grep {bamFile} {settings.BAM_PATH_FILE}").readlines()
            if len(bamFile) == 0:
                return JsonResponse({"error": "BAM file not found in the path"}, status=404)
            else:
                bamFile = bamFile[0].strip()
        locus = data['locus']
        pos = locus.split(":")[1].split("-")
        chrom = locus.split(":")[0]
        if len(pos) == 1:
            pos = int(pos[0])
            locus = f"{chrom}:{pos-10}-{pos+10}"
        base_dir = settings.BASE_DIR
        bam = bamFile.split("/")[-1]
        bamout = f"{base_dir}/apps/bamView/static/bams/{bam}"
        cmd = f"rm -rf {base_dir}/apps/bamView/static/bams/{bam}*\n"
        cmd += f"{samtools} view -h -b {bamFile} {locus} -o {bamout}\n"
        cmd += f"{samtools} index {bamout}\n"
        run(cmd, shell=True)
        data = {
            "bamFile":bamout,
            "locus":locus,
        }
        return JsonResponse(data)
    return JsonResponse({"error": "invalid request"}, status=405)
    # bam_file = request.GET.get('filename')
    # bam_file = os.path.abspath(bam_file)
    # base_dir = settings.BASE_DIR
    # bamout = f"{base_dir}/apps/bamView/static/bam/{bam_file}"
    # cmd = f"samtools view -h -b {bam_file} {loc} -o {bamout}\n"
    # cmd += f"samtools index {bamout}\n"
    # call(cmd, shell=True)
    # if bam_file:
    #     # 确保文件以 .bam 结尾
    #     if not bam_file.endswith('.bam'):
    #         bam_file += '.bam'
    #     bam_path = os.path.join(settings.BAM_DIRECTORY, bam_file)
    #     # 检查文件是否存在
    #     if os.path.exists(bam_path):
    #         with open(bam_path, 'rb') as f:
    #             response = HttpResponse(f.read(), content_type='application/octet-stream')
    #             response['Content-Disposition'] = f'attachment; filename="{bam_file}"'
    #             return response
    #     else:
    #         return HttpResponse(f"BAM file not found,{bam_path}", status=405)
    # return HttpResponse("Filename not provided", status=400)

def get_bai(request):
    bai_file = request.GET.get('filename')
    if bai_file:
        # 自动将 .bam 替换为 .bai 后缀
        bai_file = bai_file if bai_file.endswith('.bai') else bai_file + '.bai'
        bai_path = os.path.join(settings.BAM_DIRECTORY, bai_file)
        if os.path.exists(bai_path):
            with open(bai_path, 'rb') as f:
                response = HttpResponse(f.read(), content_type='application/octet-stream')
                response['Content-Disposition'] = f'attachment; filename="{bai_file}"'
                return response
        return HttpResponse("BAI file not found", status=404)
    return HttpResponse("Filename not provided", status=400)



