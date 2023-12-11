import unstructured.partition.pdf as pdf

partitioned_elements = pdf.partition_pdf(
    "test.pdf",
    include_page_breaks=True,
    strategy="hi_res",
    infer_table_structure=True,
    extract_images_in_pdf=True,
    output_type="dict",
    image_output_dir_path="images",
)
