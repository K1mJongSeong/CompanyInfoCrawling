import RegisterContainer from "@/containers/auth/RegisterContainer";

export function generateMetadata() {
  return {
    title: `Join | Sentinel Korea KYC`,
  };
}
export default function RegisterPage() {
  return <RegisterContainer />;
}
