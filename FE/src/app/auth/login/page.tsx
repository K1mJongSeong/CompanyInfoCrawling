import LoginContainer from "@/containers/auth/LoginContainer";
export function generateMetadata() {
  return {
    title: `Login | Sentinel Korea KYC`,
  };
}
export default function LoginPage() {
  return <LoginContainer />;
}
