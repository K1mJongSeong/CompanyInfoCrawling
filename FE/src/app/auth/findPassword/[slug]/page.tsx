import FindPWContainer from "@/containers/auth/FindPWContainer";

type Props = {
  params: {
    slug: string;
  };
};
export function generateMetadata({ params }: Props) {
  return {
    title: `Find Password ${params.slug} | Sentinel Korea KYC`,
  };
}

export default function FindPWpage() {
  return <FindPWContainer />;
}
export async function generateStaticParams() {
  //ssg
  const process = ["1", "2", "3"];
  return process.map((pr) => ({
    slug: pr,
  }));
}
