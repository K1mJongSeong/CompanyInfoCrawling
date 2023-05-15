import AccountContainer from "@/containers/account/AccountContainer";
import { getUserInfo } from "@/service/account_service";

type Props = {
  params: {
    id: string;
  };
};
const AccountPage = async ({ params: { id } }: Props) => {
  const result = await getUserInfo({
    email: decodeURI(decodeURIComponent(id)),
  });

  return <AccountContainer id={id} data={result} />;
};
export default AccountPage;
