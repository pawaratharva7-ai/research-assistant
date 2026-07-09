import sqlite3
from datetime import datetime
from typing import Optional
from app.api.schemas import ResearchStatus, ResearchResult

DB_PATH = "research_jobs.db"

def init_db():
    """Create the jobs table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id TEXT PRIMARY KEY,
            topic TEXT NOT NULL,
            status TEXT NOT NULL,
            report_markdown TEXT,
            error TEXT,
            created_at TEXT NOT NULL,
            completed_at TEXT
        )
    """)
    conn.commit()
    conn.close()

def create_job(job_id: str, topic: str):
    """Create a new job entry."""
    conn = sqlite3.connect(DB_PATH)
    now = datetime.utcnow().isoformat()
    conn.execute(
        "INSERT INTO jobs (id, topic, status, created_at) VALUES (?, ?, ?, ?)",
        (job_id, topic, "pending", now)
    )
    conn.commit()
    conn.close()

def get_job(job_id: str) -> Optional[ResearchResult]:
    """Retrieve a job by ID."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    row = conn.execute("SELECT * FROM jobs WHERE id = ?", (job_id,)).fetchone()
    conn.close()
    if not row:
        return None
    return ResearchResult(
        id=row["id"],
        status=row["status"],
        topic=row["topic"],
        report_markdown=row["report_markdown"],
        error=row["error"],
        created_at=datetime.fromisoformat(row["created_at"]),
        completed_at=datetime.fromisoformat(row["completed_at"]) if row["completed_at"] else None,
    )

def update_job_result(job_id: str, status: str, report: Optional[str] = None, error: Optional[str] = None):
    """Update job status and result."""
    conn = sqlite3.connect(DB_PATH)
    now = datetime.utcnow().isoformat()
    conn.execute(
        """UPDATE jobs 
           SET status = ?, report_markdown = ?, error = ?, completed_at = ? 
           WHERE id = ?""",
        (status, report, error, now if status in ("completed", "failed") else None, job_id)
    )
    conn.commit()
    conn.close()