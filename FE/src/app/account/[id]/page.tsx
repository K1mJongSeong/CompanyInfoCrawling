import AccountContainer from "@/containers/account/AccountContainer";

type Props = {
  params: {
    id: string;
  };
};
export default function AccountPage({ params: { id } }: Props) {
  return <AccountContainer id={id} />;
}
