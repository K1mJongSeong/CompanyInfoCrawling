import BgContainer from "@/components/common/BgContainer";

export default function AuthLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return <BgContainer>{children}</BgContainer>;
}
