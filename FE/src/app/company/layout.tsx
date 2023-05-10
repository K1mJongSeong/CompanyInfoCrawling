import CaompanyLayout from "@/components/company/common/CaompanyLayout";
import { Metadata } from "next/types";

export const metadata: Metadata = {
  title: "Company | Sentinel Korea KYC",
  description: "Enterprise Information Delivery Platform | Sentinel Korea KYC",
};

export default function AuthLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return <CaompanyLayout>{children}</CaompanyLayout>;
}
