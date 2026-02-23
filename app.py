# import PyPDF2

# pdfFiles = ["1.pdf", "2.pdf"]

# merger = PyPDF2.PdfMerger()

# for filename in pdfFiles:
#     with open(filename, "rb") as pdfFile:
#         reader = PyPDF2.PdfReader(pdfFile)
#         merger.append(reader)

# merger.write("merged.pdf")
# merger.close()

# print("PDFs merged successfully 🎉")

import streamlit as st
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

st.set_page_config(page_title="PDFusion", page_icon="📄")

st.title("📄 PDFusion – PDF Merger & Slicer")
st.write("Merge multiple PDFs or slice selected pages from a PDF.")

# Two sections
option = st.radio(
    "Choose an operation:",
    ("Merge PDFs", "Slice PDF")
)

# -------------------- MERGE PDFs --------------------
if option == "Merge PDFs":
    st.subheader("🔗 Merge Multiple PDFs")

    uploaded_files = st.file_uploader(
        "Upload PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )

    if st.button("Merge PDFs"):
        if uploaded_files and len(uploaded_files) >= 2:
            merger = PdfMerger()

            for pdf in uploaded_files:
                merger.append(pdf)

            with open("merged.pdf", "wb") as f:
                merger.write(f)

            st.success("PDFs merged successfully 🎉")

            with open("merged.pdf", "rb") as f:
                st.download_button(
                    "⬇️ Download Merged PDF",
                    f,
                    file_name="merged.pdf",
                    mime="application/pdf"
                )
        else:
            st.warning("Please upload at least TWO PDF files.")

# -------------------- SLICE PDF --------------------
elif option == "Slice PDF":
    st.subheader("✂️ Slice PDF Pages")

    uploaded_pdf = st.file_uploader(
        "Upload a PDF",
        type=["pdf"]
    )

    if uploaded_pdf:
        reader = PdfReader(uploaded_pdf)
        total_pages = len(reader.pages)

        st.info(f"Total pages in PDF: {total_pages}")

        start_page = st.number_input(
            "Start Page",
            min_value=1,
            max_value=total_pages,
            value=1
        )

        end_page = st.number_input(
            "End Page",
            min_value=start_page,
            max_value=total_pages,
            value=total_pages
        )

        if st.button("Slice PDF"):
            writer = PdfWriter()

            for i in range(start_page - 1, end_page):
                writer.add_page(reader.pages[i])

            with open("sliced.pdf", "wb") as f:
                writer.write(f)

            st.success("PDF sliced successfully ✂️")

            with open("sliced.pdf", "rb") as f:
                st.download_button(
                    "⬇️ Download Sliced PDF",
                    f,
                    file_name="sliced.pdf",
                    mime="application/pdf"
                )