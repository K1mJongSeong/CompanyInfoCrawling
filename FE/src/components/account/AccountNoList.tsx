export default function AccountNoList({ message }: { message: string }) {
  return (
    <div className="w-full min-h-[124px] flex justify-center items-center text-xs text-gray-500">
      {message}
    </div>
  );
}
