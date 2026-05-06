// Reusable UI components: Icon, BottomBar, KPI cards, Charts, Tables, Badges
const { useState, useMemo, useEffect, useRef } = React;

/* -------------------- ICONS (clean line, 1.5 stroke) -------------------- */
function Icon({ name, size = 20, stroke = 'currentColor' }) {
  const props = { width: size, height: size, viewBox: '0 0 24 24', fill: 'none', stroke, strokeWidth: 1.6, strokeLinecap: 'round', strokeLinejoin: 'round' };
  switch (name) {
    case 'dashboard': return <svg {...props}><rect x="3" y="3" width="7" height="9" rx="1.5"/><rect x="14" y="3" width="7" height="5" rx="1.5"/><rect x="14" y="12" width="7" height="9" rx="1.5"/><rect x="3" y="16" width="7" height="5" rx="1.5"/></svg>;
    case 'projects': return <svg {...props}><path d="M3 7.5A1.5 1.5 0 0 1 4.5 6h4l2 2h9A1.5 1.5 0 0 1 21 9.5V18a1.5 1.5 0 0 1-1.5 1.5h-15A1.5 1.5 0 0 1 3 18z"/></svg>;
    case 'plus': return <svg {...props}><path d="M12 5v14M5 12h14"/></svg>;
    case 'catalog': return <svg {...props}><path d="M4 4h7v16H4zM13 4h7v16h-7z"/><path d="M7.5 8h0M16.5 8h0"/></svg>;
    case 'reports': return <svg {...props}><path d="M3 20h18"/><rect x="5" y="11" width="3" height="7"/><rect x="10.5" y="7" width="3" height="11"/><rect x="16" y="13" width="3" height="5"/></svg>;
    case 'search': return <svg {...props}><circle cx="11" cy="11" r="6.5"/><path d="m20 20-3.5-3.5"/></svg>;
    case 'bell': return <svg {...props}><path d="M6 8a6 6 0 1 1 12 0c0 5 2 6 2 6H4s2-1 2-6"/><path d="M10 19a2 2 0 0 0 4 0"/></svg>;
    case 'filter': return <svg {...props}><path d="M3 5h18l-7 8v6l-4 2v-8z"/></svg>;
    case 'export': return <svg {...props}><path d="M12 3v12M7 8l5-5 5 5"/><path d="M5 21h14"/></svg>;
    case 'edit': return <svg {...props}><path d="M4 20h4l11-11-4-4L4 16z"/><path d="M14 5l4 4"/></svg>;
    case 'trash': return <svg {...props}><path d="M4 7h16M9 7V4h6v3M6 7l1 13h10l1-13"/></svg>;
    case 'check': return <svg {...props}><path d="M5 12l5 5 9-11"/></svg>;
    case 'arrow-up': return <svg {...props}><path d="M12 19V5M6 11l6-6 6 6"/></svg>;
    case 'arrow-down': return <svg {...props}><path d="M12 5v14M6 13l6 6 6-6"/></svg>;
    case 'chevron-back': return <svg {...props}><path d="M15 6l-6 6 6 6"/></svg>;
    case 'menu': return <svg {...props}><path d="M4 7h16M4 12h16M4 17h16"/></svg>;
    case 'user': return <svg {...props}><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-7 8-7s8 3 8 7"/></svg>;
    case 'wallet': return <svg {...props}><rect x="3" y="6" width="18" height="13" rx="2"/><path d="M16 12.5h3"/><path d="M3 9h15a3 3 0 0 1 0 6H3"/></svg>;
    case 'briefcase': return <svg {...props}><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2"/></svg>;
    case 'percent': return <svg {...props}><path d="M19 5L5 19"/><circle cx="7" cy="7" r="2"/><circle cx="17" cy="17" r="2"/></svg>;
    case 'clock': return <svg {...props}><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>;
    case 'bolt': return <svg {...props}><path d="M13 2L4 14h7l-1 8 9-12h-7z"/></svg>;
    case 'pdf': return <svg {...props}><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><path d="M9 13h2M9 16h6"/></svg>;
    case 'excel': return <svg {...props}><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M9 8l6 8M15 8l-6 8"/></svg>;
    case 'dots': return <svg {...props}><circle cx="5" cy="12" r="1"/><circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/></svg>;
    case 'close': return <svg {...props}><path d="M6 6l12 12M18 6L6 18"/></svg>;
    case 'eye': return <svg {...props}><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></svg>;
    case 'spark': return <svg {...props}><path d="M12 3l1.8 5.4L19 10l-5.2 1.6L12 17l-1.8-5.4L5 10l5.2-1.6z"/></svg>;
    default: return null;
  }
}

/* -------------------- BADGE -------------------- */
function Badge({ children, tone = 'neutral', dot }) {
  const map = {
    pos: { bg: 'var(--pos-bg)', fg: 'var(--pos)' },
    warn: { bg: 'var(--warn-bg)', fg: 'var(--warn)' },
    neg: { bg: 'var(--neg-bg)', fg: 'var(--neg)' },
    info: { bg: 'var(--info-bg)', fg: 'var(--info)' },
    neutral: { bg: 'var(--bg-soft)', fg: 'var(--ink-2)' },
  };
  const t = map[tone] || map.neutral;
  return (
    <span style={{
      display: 'inline-flex', alignItems: 'center', gap: 6,
      padding: '3px 9px', borderRadius: 999, fontSize: 11.5, fontWeight: 500,
      background: t.bg, color: t.fg, lineHeight: 1.4, whiteSpace: 'nowrap',
    }}>
      {dot && <span style={{ width: 6, height: 6, borderRadius: 999, background: t.fg }} />}
      {children}
    </span>
  );
}

function statusToTone(s) {
  if (s === 'مكتمل') return 'pos';
  if (s === 'قيد التنفيذ') return 'info';
  if (s === 'بانتظار الموافقة') return 'warn';
  if (s === 'مسودة') return 'neutral';
  return 'neutral';
}

/* -------------------- BOTTOM BAR -------------------- */
function BottomBar({ active, onChange, variant = 'a' }) {
  const items = window.APP_DATA.bottomNav;
  const isB = variant === 'b';
  return (
    <nav
      role="tablist"
      style={{
        position: 'relative',
        flexShrink: 0,
        background: isB ? 'var(--surface)' : 'var(--surface)',
        borderTop: `1px solid var(--line)`,
        padding: '8px 8px calc(8px + env(safe-area-inset-bottom, 0px))',
        boxShadow: isB ? '0 -8px 30px rgba(15,20,40,0.06)' : '0 -1px 0 var(--line)',
      }}
    >
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(5, 1fr)', gap: 4 }}>
        {items.map((it) => {
          const isActive = active === it.id;
          if (it.primary) {
            // Primary FAB-style center
            return (
              <button
                key={it.id}
                onClick={() => onChange(it.id)}
                aria-label={it.label}
                style={{
                  position: 'relative',
                  border: 'none', cursor: 'pointer',
                  display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center',
                  background: 'transparent', padding: '0 0 4px',
                }}
              >
                <span style={{
                  width: 46, height: 46, borderRadius: isB ? 14 : 999,
                  background: isB ? 'var(--accent-2, var(--ink))' : 'var(--ink)',
                  color: isB ? '#1B1F2A' : 'var(--bg)',
                  display: 'flex', alignItems: 'center', justifyContent: 'center',
                  marginBottom: 4,
                  boxShadow: isB ? '0 6px 18px rgba(198,138,46,0.35)' : '0 4px 14px rgba(0,0,0,0.18)',
                  transform: isActive ? 'translateY(-2px)' : 'translateY(0)',
                  transition: 'transform .15s ease',
                }}>
                  <Icon name={it.icon} size={22} />
                </span>
                <span style={{ fontSize: 10.5, fontWeight: 500, color: 'var(--ink-3)' }}>{it.label}</span>
              </button>
            );
          }
          return (
            <button
              key={it.id}
              onClick={() => onChange(it.id)}
              aria-label={it.label}
              role="tab"
              aria-selected={isActive}
              style={{
                position: 'relative',
                border: 'none', cursor: 'pointer', background: 'transparent',
                display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center',
                padding: '8px 4px 4px',
                color: isActive ? 'var(--ink)' : 'var(--ink-3)',
                gap: 4,
              }}
            >
              {isB && isActive && (
                <span style={{
                  position: 'absolute', top: 0, left: '20%', right: '20%', height: 2,
                  background: 'var(--accent-2, var(--ink))', borderRadius: 99,
                }} />
              )}
              <Icon name={it.icon} size={22} stroke={isActive ? 'currentColor' : 'var(--ink-3)'} />
              <span style={{ fontSize: 10.5, fontWeight: isActive ? 600 : 500 }}>{it.label}</span>
              {!isB && isActive && (
                <span style={{ width: 4, height: 4, borderRadius: 999, background: 'var(--ink)' }} />
              )}
            </button>
          );
        })}
      </div>
    </nav>
  );
}

/* -------------------- KPI CARD -------------------- */
function KpiCard({ label, value, sub, trend, icon, accentB }) {
  const positive = trend && trend.startsWith('+');
  return (
    <div style={{
      background: 'var(--surface)',
      border: '1px solid var(--line)',
      borderRadius: 14,
      padding: 14,
      display: 'flex', flexDirection: 'column', gap: 10,
      minHeight: 108,
    }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <span style={{ fontSize: 12, color: 'var(--ink-3)', fontWeight: 500 }}>{label}</span>
        <span style={{
          width: 28, height: 28, borderRadius: 8,
          background: accentB ? 'var(--accent-soft)' : 'var(--bg-soft)',
          color: accentB ? 'var(--accent, var(--ink))' : 'var(--ink-2)',
          display: 'flex', alignItems: 'center', justifyContent: 'center',
        }}><Icon name={icon} size={15}/></span>
      </div>
      <div className="num" style={{ fontSize: 24, fontWeight: 700, lineHeight: 1.1, letterSpacing: '-0.02em' }}>{value}</div>
      <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
        {trend && (
          <span style={{
            display: 'inline-flex', alignItems: 'center', gap: 2,
            fontSize: 11, fontWeight: 600,
            color: positive ? 'var(--pos)' : 'var(--neg)',
          }}>
            <Icon name={positive ? 'arrow-up' : 'arrow-down'} size={11} />
            {trend}
          </span>
        )}
        <span style={{ fontSize: 11, color: 'var(--ink-3)' }}>{sub}</span>
      </div>
    </div>
  );
}

/* -------------------- LINE / AREA CHART (revenue) -------------------- */
function RevenueChart({ data, accent = 'var(--ink)', height = 180, variant = 'a' }) {
  const W = 600, H = height, padX = 28, padY = 28;
  const max = Math.max(...data.map(d => d.v));
  const min = Math.min(...data.map(d => d.v));
  const range = max - min || 1;
  const stepX = (W - padX * 2) / (data.length - 1);
  const points = data.map((d, i) => ({
    x: padX + i * stepX,
    y: padY + (1 - (d.v - min) / range) * (H - padY * 2),
    v: d.v, m: d.m,
  }));
  const path = points.map((p, i) => `${i ? 'L' : 'M'}${p.x.toFixed(1)} ${p.y.toFixed(1)}`).join(' ');
  const areaPath = `${path} L${points[points.length-1].x} ${H - padY} L${points[0].x} ${H - padY} Z`;

  const [hover, setHover] = useState(null);
  return (
    <svg viewBox={`0 0 ${W} ${H}`} style={{ width: '100%', height: H, display: 'block' }} onMouseLeave={() => setHover(null)}>
      <defs>
        <linearGradient id={`area-${variant}`} x1="0" x2="0" y1="0" y2="1">
          <stop offset="0%" stopColor={accent} stopOpacity={variant === 'b' ? 0.25 : 0.18} />
          <stop offset="100%" stopColor={accent} stopOpacity="0" />
        </linearGradient>
      </defs>
      {/* gridlines */}
      {[0,1,2,3].map(i => {
        const y = padY + (i/3) * (H - padY*2);
        return <line key={i} x1={padX} x2={W-padX} y1={y} y2={y} stroke="var(--line)" strokeDasharray="2 4" />;
      })}
      <path d={areaPath} fill={`url(#area-${variant})`} />
      <path d={path} fill="none" stroke={accent} strokeWidth="2" strokeLinejoin="round" strokeLinecap="round" />
      {points.map((p, i) => (
        <g key={i} onMouseEnter={() => setHover(i)} style={{ cursor: 'pointer' }}>
          <circle cx={p.x} cy={p.y} r="10" fill="transparent" />
          <circle cx={p.x} cy={p.y} r={hover === i ? 5 : 3} fill="var(--surface)" stroke={accent} strokeWidth="2" />
          <text x={p.x} y={H - 6} textAnchor="middle" fontSize="10" fill="var(--ink-3)" style={{ fontFamily: 'inherit' }}>{p.m.slice(0, 4)}</text>
        </g>
      ))}
      {hover !== null && (
        <g>
          <line x1={points[hover].x} x2={points[hover].x} y1={padY} y2={H-padY} stroke={accent} strokeOpacity="0.25" strokeDasharray="3 3" />
          <rect x={points[hover].x - 30} y={points[hover].y - 32} width="60" height="22" rx="6" fill="var(--ink)" />
          <text x={points[hover].x} y={points[hover].y - 17} textAnchor="middle" fontSize="11" fontWeight="600" fill="var(--bg)">{points[hover].v}ك ر.س</text>
        </g>
      )}
    </svg>
  );
}

/* -------------------- DONUT CHART -------------------- */
function Donut({ data, size = 140, thickness = 18, centerLabel, centerValue }) {
  const total = data.reduce((s, d) => s + d.value, 0);
  const r = (size - thickness) / 2;
  const c = size / 2;
  const circ = 2 * Math.PI * r;
  let offset = 0;
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
      <svg width={size} height={size} viewBox={`0 0 ${size} ${size}`} style={{ transform: 'rotate(-90deg)', flexShrink: 0 }}>
        <circle cx={c} cy={c} r={r} fill="none" stroke="var(--bg-soft)" strokeWidth={thickness} />
        {data.map((d, i) => {
          const len = (d.value / total) * circ;
          const seg = (
            <circle
              key={i}
              cx={c} cy={c} r={r}
              fill="none"
              stroke={d.color}
              strokeWidth={thickness}
              strokeDasharray={`${len} ${circ - len}`}
              strokeDashoffset={-offset}
              strokeLinecap="butt"
            />
          );
          offset += len;
          return seg;
        })}
        {centerValue && (
          <g transform={`rotate(90 ${c} ${c})`}>
            <text x={c} y={c-2} textAnchor="middle" fontSize="18" fontWeight="700" fill="var(--ink)" style={{ fontFamily: 'inherit' }}>{centerValue}</text>
            <text x={c} y={c+14} textAnchor="middle" fontSize="10" fill="var(--ink-3)" style={{ fontFamily: 'inherit' }}>{centerLabel}</text>
          </g>
        )}
      </svg>
      <div style={{ display: 'flex', flexDirection: 'column', gap: 8, flex: 1, minWidth: 0 }}>
        {data.map((d, i) => (
          <div key={i} style={{ display: 'flex', alignItems: 'center', gap: 8, fontSize: 12 }}>
            <span style={{ width: 8, height: 8, borderRadius: 2, background: d.color, flexShrink: 0 }} />
            <span style={{ color: 'var(--ink-2)', flex: 1 }}>{d.label}</span>
            <span className="num" style={{ color: 'var(--ink)', fontWeight: 600 }}>{d.value}%</span>
          </div>
        ))}
      </div>
    </div>
  );
}

/* -------------------- BAR CHART (compact) -------------------- */
function BarChart({ data, height = 160 }) {
  const max = Math.max(...data.map(d => d.v));
  return (
    <div style={{ display: 'flex', alignItems: 'flex-end', gap: 8, height, padding: '0 4px' }}>
      {data.map((d, i) => {
        const h = (d.v / max) * (height - 28);
        return (
          <div key={i} style={{ flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 6 }}>
            <span className="num" style={{ fontSize: 10, color: 'var(--ink-3)' }}>{d.v}</span>
            <div style={{
              width: '100%', height: h, borderRadius: '4px 4px 2px 2px',
              background: i === data.length - 1 ? 'var(--ink)' : 'var(--line-strong)',
              transition: 'height .3s ease',
            }} />
            <span style={{ fontSize: 10, color: 'var(--ink-3)' }}>{d.m.slice(0, 3)}</span>
          </div>
        );
      })}
    </div>
  );
}

/* -------------------- SECTION HEADER -------------------- */
function SectionHeader({ title, subtitle, action }) {
  return (
    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 12 }}>
      <div>
        <h3 style={{ margin: 0, fontSize: 15, fontWeight: 700, letterSpacing: '-0.01em' }}>{title}</h3>
        {subtitle && <div style={{ fontSize: 11.5, color: 'var(--ink-3)', marginTop: 2 }}>{subtitle}</div>}
      </div>
      {action}
    </div>
  );
}

/* -------------------- TOP BAR -------------------- */
function TopBar({ title, subtitle, back, action, variant = 'a' }) {
  return (
    <header style={{
      flexShrink: 0,
      padding: '14px 16px 10px',
      background: variant === 'b' ? 'var(--surface)' : 'var(--bg)',
      borderBottom: variant === 'b' ? '1px solid var(--line)' : 'none',
      display: 'flex', alignItems: 'center', gap: 10,
    }}>
      {back ? (
        <button onClick={back} style={{ width: 36, height: 36, border: '1px solid var(--line)', borderRadius: 10, background: 'var(--surface)', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', color: 'var(--ink-2)' }}>
          <Icon name="chevron-back" size={18} />
        </button>
      ) : (
        <div style={{ width: 36, height: 36, borderRadius: 10, background: variant === 'b' ? 'var(--accent)' : 'var(--ink)', color: variant === 'b' ? 'var(--accent-2)' : 'var(--bg)', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 700, fontSize: 14 }}>
          <Icon name="bolt" size={17} />
        </div>
      )}
      <div style={{ flex: 1, minWidth: 0 }}>
        <h1 style={{ margin: 0, fontSize: 16, fontWeight: 700, letterSpacing: '-0.01em', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>{title}</h1>
        {subtitle && <div style={{ fontSize: 11.5, color: 'var(--ink-3)', marginTop: 1 }}>{subtitle}</div>}
      </div>
      {action || (
        <>
          <button style={{ width: 36, height: 36, border: '1px solid var(--line)', borderRadius: 10, background: 'var(--surface)', cursor: 'pointer', color: 'var(--ink-2)' }}>
            <Icon name="search" size={17} />
          </button>
          <button style={{ width: 36, height: 36, border: '1px solid var(--line)', borderRadius: 10, background: 'var(--surface)', cursor: 'pointer', color: 'var(--ink-2)', position: 'relative' }}>
            <Icon name="bell" size={17} />
            <span style={{ position: 'absolute', top: 7, right: 8, width: 7, height: 7, borderRadius: 999, background: 'var(--warn, #B25D2B)' }} />
          </button>
        </>
      )}
    </header>
  );
}

Object.assign(window, { Icon, Badge, statusToTone, BottomBar, KpiCard, RevenueChart, Donut, BarChart, SectionHeader, TopBar });
