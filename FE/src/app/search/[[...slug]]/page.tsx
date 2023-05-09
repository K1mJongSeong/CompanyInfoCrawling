interface Props {
  params: {
    slug: string | Array<string>;
  };
}
export default function SearchPage({ params: { slug } }: Props) {
  return <div>{slug}</div>;
}
