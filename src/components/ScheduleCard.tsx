export default function ScheduleCard({
  schedule,
}: {
  schedule: {
    id: number;
    date: string;
    start_time: string;
    end_time: string;
    available: boolean;
    court_id: number;
  };
}) {
  return (
    <div
      className={`flex items-center gap-3 p-3 rounded-lg shadow-sm bg-white hover:bg-gray-50 ${
        schedule.available ? "cursor-pointer" : "cursor-not-allowed opacity-60"
      }`}
    >
      <div
        className={`px-3 py-2 rounded-md text-sm font-medium ${
          schedule.available
            ? "chip-available"
            : "chip-occupied"
        }`}
      >
        <div className="text-sm">
          {schedule.start_time} às {schedule.end_time}
        </div>
      </div>
      <div className="text-sm text-gray-600">
        {schedule.available ? (
          <span style={{ color: "var(--brand-600)" }} className="font-semibold">
            Disponível
          </span>
        ) : (
          <span>Ocupado</span>
        )}
      </div>
    </div>
  );
}
