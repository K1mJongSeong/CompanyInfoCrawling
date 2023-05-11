"use client";
import { BlobProvider } from "@react-pdf/renderer";
import { useState } from "react";
import RepoerPDF from "./RepoerPDF";
import { Document, Page, pdfjs } from "react-pdf";
import { PDFDocumentProxy } from "pdfjs-dist/types/src/display/api";
import Link from "next/link";
import { MobilePDFReader } from "react-read-pdf";

const options = {
  cMapUrl: "cmaps/",
  standardFontDataUrl: "standard_fonts/",
};

export default function ReportTest() {
  const [_pdf, setPdf] = useState<PDFDocumentProxy | null>(null);
  const [_blob, setBlob] = useState<Blob | null>(null);
  const [pageNum, setPageNum] = useState<number>(0);
  const handleLoadSuccess = (pdf: PDFDocumentProxy, blob: Blob | null) => {
    setPdf(pdf);
    setBlob(blob);
    setPageNum(pdf.numPages);
  };
  const [_url, setUrl] = useState<string>("");
  return (
    <>
      <BlobProvider document={<RepoerPDF />}>
        {({ blob, url, loading }) => {
          if (url) {
            setUrl(url);
            return (
              <Link href={url} target="_blank">
                {url}
              </Link>
            );
          }
        }}
      </BlobProvider>
      {_url && <MobilePDFReader url={_url} />}
    </>
  );
}
