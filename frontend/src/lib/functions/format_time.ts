const units = [
  { label: 'yr', seconds: 31536000 },
  { label: 'mo', seconds: 2592000 },
  { label: 'wk', seconds: 604800 },
  { label: 'd', seconds: 86400 },
  { label: 'hr', seconds: 3600 },
  { label: 'min', seconds: 60 },
  { label: 's', seconds: 1 }
];

export function format_time(date: number | string | Date) {
  const diff_time = calculate_time_diff(date);
  if (diff_time <= 0) return 'just now';

  const { interval, label } = get_time_unit(diff_time);
  return `${interval}${label} ago`;
}

function calculate_time_diff(date: number | string | Date) {
  const time = Math.floor((new Date().valueOf() - new Date(date).valueOf()) / 1000);
  return time;
}

function get_time_unit(time: number) {
  for (const { label, seconds } of units) {
    const interval = Math.floor(time / seconds);
    if (interval >= 1) {
      return { interval, label };
    }
  }
  return { interval: 0, label: '' };
}
