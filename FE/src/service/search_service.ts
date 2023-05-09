import { AppRouterInstance } from "next/dist/shared/lib/app-router-context";
import { EnqueueSnackbar } from "notistack";

interface BasicProps {
  e: React.FormEvent;
  value: string;
  router: AppRouterInstance;
  enqueueSnackbar: EnqueueSnackbar;
}
export function GotoSearch(props: BasicProps) {
  const { e, value, router, enqueueSnackbar } = props;
  e.preventDefault();
  if (!value) {
    enqueueSnackbar("Please enter the keyword you want to search", {
      variant: "warning",
    });
    return;
  }
  router.push(`/search/${value}`);
}
