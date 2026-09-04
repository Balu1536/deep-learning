# -*- coding: utf-8 -*-
"""Helper functions to build topic HTML blocks consistently."""

PRIORITY_MAP = {
    'VH': ('vh', '🔥 VERY HIGH PRIORITY'),
    'H':  ('h',  '🟠 HIGH PRIORITY'),
    'M':  ('m',  '🟡 MEDIUM PRIORITY'),
    'L':  ('l',  '🟢 LOW PRIORITY'),
}

def topic(id_, title, priority, body_html):
    """body_html: full inner HTML (subsections already formatted by caller)."""
    cls, label = PRIORITY_MAP[priority]
    return f'''
  <div class="topic" id="{id_}">
    <div class="topic-head">
      <h3>{title}</h3>
      <div class="topic-controls">
        <span class="badge {cls}">{label}</span>
        <button class="progress-btn" data-id="{id_}" onclick="cycleProgress('{id_}')">☐ Not Started</button>
        <button class="bookmark-btn" data-id="{id_}" onclick="toggleBookmark('{id_}')">☆</button>
      </div>
    </div>
    {body_html}
  </div>
'''

def sub(label):
    return f'<div class="subhead">{label}</div>'

def box(kind, html):
    return f'<div class="box {kind}">{html}</div>'

def chapter_header(id_, title):
    return f'<div class="chapter-header" id="{id_}"><h2>{title}</h2></div>'

def unit_banner(title, desc):
    return f'<div class="unit-banner"><h1>{title}</h1><p>{desc}</p></div>'

def revision_box(id_, title, inner_html):
    return f'<div class="revision-box" id="{id_}"><h2>{title}</h2>{inner_html}</div>'
